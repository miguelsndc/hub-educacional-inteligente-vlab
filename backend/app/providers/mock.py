from app.schemas.ai import AIResponse


class MockProvider:
    def suggest(self, prompt: str, user_message: str, title: str) -> AIResponse:
        return AIResponse(
            description="Este é um material educacional gerado pelo provider mock para fins de desenvolvimento.",
            tags=["mock", "dev", "teste"],
        )
