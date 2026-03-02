from app.constants import AIProviderEnum
from app.settings import Settings


def get_provider(settings: Settings) -> AIProviderEnum:
    match settings.AI_PROVIDER:
        case AIProviderEnum.GEMINI:
            from app.providers.gemini import GeminiProvider

            return GeminiProvider(settings.GEMINI_API_KEY, settings.GEMINI_MODEL)
        case AIProviderEnum.ANTHROPIC:
            from app.providers.mock import AnthropicProvider

            return AnthropicProvider(settings.ANTHROPIC_API_KEY)
        case AIProviderEnum.MOCK:
            from app.providers.mock import MockProvider

            return MockProvider()
        case _:
            raise ValueError(f"Unsupported AI provider: {settings.AI_PROVIDER}")
