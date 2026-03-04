class AppError(Exception):
    """Classe base para exceções da aplicação."""

    pass


class ResourceNotFoundError(AppError):
    """Exceção lançada quando um recurso não é encontrado."""

    def __init__(self, resource_id: int):
        self.resource_id = resource_id
        super().__init__(f"Recurso com id: {resource_id} não encontrado.")


class AIProviderError(AppError):
    """Exceção para erros relacionados ao provedor de IA."""

    def __init__(self, message: str):
        super().__init__(f"Erro Provedor de IA: {message}")


class AITimeoutError(AIProviderError):
    def __init__(self):
        super().__init__("Provedor de IA expirou. Tente novamente mais tarde.")


class AIResponseParseError(AIProviderError):
    def __init__(self, raw: str):
        self.raw = raw
        super().__init__(
            f"Provedor de IA retornou um formato de resposta inesperado: {raw}"
        )
