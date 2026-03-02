# Sprint 1 — Backend CRUD

**Objetivo:** API REST funcional para gerenciamento de recursos educacionais.  
**Estimativa:** 4–5 horas

---

## Escopo

Implementar as operações de CRUD dos recursos educacionais. A listagem deve ser paginada e todos os dados devem ser validados antes de persistir.

Os campos de um recurso são: título, descrição, tipo (vídeo, pdf ou link), url e tags.

---

## O que precisa ser feito

- Modelar o recurso no banco via SQLAlchemy
- Definir os schemas de entrada e saída com Pydantic
- Implementar a camada de serviço com as operações do CRUD
- Expor os endpoints REST
- Registrar o router no `main.py`

---

## Comportamentos esperados

- Requisições com dados inválidos retornam erro descritivo
- Recursos inexistentes retornam 404
- A listagem retorna metadados de paginação junto com os itens
- A exclusão não retorna corpo, apenas status 204

---

## Checklist

- [ ] Tabela criada automaticamente ao subir o backend
- [ ] Todos os endpoints respondem corretamente
- [ ] Validações funcionando — título vazio e tipo inválido são rejeitados
- [ ] Paginação retorna metadados corretos
- [ ] Testado manualmente via Swagger em `/docs`

---

**Próxima sprint:** Sprint 2 — Frontend + Smart Assist