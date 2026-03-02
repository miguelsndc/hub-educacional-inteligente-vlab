import json
import time
import google.generativeai as genai

from settings import settings
from app.schemas.ai import AIResponse
from app.exceptions import AIResponseParseError, AITimeoutError
from app.logger import logger


class GeminiProvider:
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    def suggest(self, prompt: str, user_message: str) -> AIResponse:
        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(model_name=self.model, system_instruction=prompt)
        start = time.perf_counter()
        try:
            response = model.generate_content(
                user_message, request_options={"timeout": settings.AI_TIMEOUT_SECONDS}
            )
        except Exception as e:
            if "timeout" in str(e).lower():
                raise AITimeoutError()
            raise

        latency = round(time.perf_counter() - start, 2)
        raw = response.text.strip()

        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            logger.error(
                "Failed to parse Gemini response as JSON", extra={"ctx_raw": raw}
            )
            return AIResponseParseError(raw)

        logger.info(
            "AI Request",
            extra={
                "ctx_title": user_message,
                "ctx_latency": latency,
                "ctx_token_usage": response.usage_metadata.total_token_count,
            },
        )

        return AIResponse(**data)
