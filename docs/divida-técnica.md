# Dívidas Técnicas

**Backend**:
- Testes automatizados das partes mais críticas do sistema
- Providers de IA além do Gemini estão como "dummies" (AnthropicProvider e OpenAIProvider) retornam strings fixas

**Frontend**

- Ausência de testes automatizados
- Mensagens de erro exibidas como parágrafo simples, sem distinção entre tipos (erro de validação vs falha de rede vs timeout)

**Produto**

- Modo de complemento na descrição inteligente: permitir que a IA complete uma descrição já existente ao invés de substituí-la direto
- Fluxo de aprovação de novas tags sugeridas pela IA (documentado no ADR-004)
- Busca e filtro por título e tags
- Tornar responsivo, até funciona mas não 100% adaptado
- Fluxo de tags (adr_002)