import json
import time
import google.generativeai as genai
from google.api_core.exceptions import DeadlineExceeded

from app.settings import settings
from app.schemas.ai import AIResponse
from app.exceptions import AIResponseParseError, AITimeoutError, AIProviderError
from app.logger import get_logger


class GeminiProvider:
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model
        self.logger = get_logger(__name__)

    def suggest(self, prompt: str, user_message: str, title: str) -> AIResponse:
        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(model_name=self.model, system_instruction=prompt)
        start = time.perf_counter()
        try:
            response = model.generate_content(
                user_message, request_options={"timeout": settings.AI_TIMEOUT_SECONDS}
            )
        except DeadlineExceeded:
            raise AITimeoutError()
        except Exception as e:
            raise AIProviderError(str(e))

        latency = round(time.perf_counter() - start, 2)
        raw = response.text.strip()

        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            self.logger.error(
                "Failed to parse Gemini response as JSON", extra={"ctx_raw": raw}
            )
            return AIResponseParseError(raw)

        self.logger.info(
            "AI Request",
            extra={
                "ctx_title": title,
                "ctx_latency": latency,
                "ctx_token_usage": int(response.usage_metadata.total_token_count),
            },
        )

        return AIResponse(**data)
