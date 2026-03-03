from typing import Protocol
from app.schemas.ai import AIResponse


"""Define a interface do provider de IA usando Protocols para garantir
que qualquer implementação tenha o método suggest com a assinatura correta.
Isso permite que o sistema seja flexível e possa facilmente integrar diferentes
provedores de IA no futuro, desde que eles implementem essa interface, também
permitindo facilmente mockar o provider para testes

A acoplação entre o schema e o provider é feita através do tipo de retorno do suggest(...), que é AIResponse.
Isso garante que qualquer mudança no schema tenha que ser refletida na implementação do provider,
mantendo a consistência entre cada parte do sistema"""


class AIProvider(Protocol):
    def suggest(self, prompt: str, user_message: str, title: str) -> AIResponse: ...
