class AppError(Exception):
    """Classe base para exceções da aplicação."""
    pass

class ResourceNotFoundError(AppError):
    """Exceção lançada quando um recurso não é encontrado."""
    def __init__(self, resource_id: int):
        self.resource_id = resource_id
        super().__init__(f"Resource with id: {resource_id} not found.")

class AIProviderError(AppError):
    """Exceção para erros relacionados ao provedor de IA."""
    def __init__(self, message: str):
        super().__init__(f"AI Provider Error: {message}")

class AITimeoutError(AIProviderError):
    def __init__(self):
        super().__init__("AI provider timed out. Try again later.")

class AIResponseParseError(AIProviderError):
    def __init__(self, raw: str):
        self.raw = raw
        super().__init__(f"AI returned an unexpected response format: {raw}")