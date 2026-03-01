# Sprint 0 - Fundação

**Objetivo**: Projeto estruturado, dockerizado e com CI configurado, nenhuma regra de negócio ainda.

**Estimativa**: 2-3 horas.

**Definição de Pronto**: `GET /health` retorna 200, frontend rodando sem erros no console, primeiro push passa o CI.

## O que precisa existir ao final dessa sprint

**Repositório e estrutura**:
-   Repositório público no Github criado
-   Estrutura de pastas definida: `frontend/`, `backend/`, `docs/` e `.github/`
-   `.gitignore` cobrindo Python, Node `.env` e arquivos de SO.  


**Backend**:
-   Projeto FastAPI Inicializado com o `uvicorn`
-   Dependências listadas em `requirements.txt` e instaladas
-   Configurações centralizadas em `pydantic-settings`, consumindo do `.env`
-   Sistema de logs estruturados com JSON, encapsulado num módulo próprio.
-   Hierarquia de erros customizadas definida
-   Endpoint `GET /health` respondendo e verificando conexões com o banco
-   CORS configurado
  
**Banco de Dados**:
-   SQLAlchemy configurado
-   Estrutura pronta para receber Alembic futuramente.
  
**Frontend**:
-   Projeto Vite + React configurado
-   Tailwind configurado
-   React query instalado
-   Axios instalado
-   Roteamento base com React Router configurado
-   Variáveis de ambiente `.env` (chaves e rotas da api)
  

**Docker**:
-   `Dockerfile` para o backend
-   `Dockerfile` para o frontend
-   Arquivo de docker compose orquestrando os dois serviços
-   Hot reload funcionando
  
**Documentação Inicial**:
-   `README.md` com título e "como rodar" básico (expandido futuramente)
-   `.env.example` com campos explicados
-   Estrutura de `docs/` criada (sprints, PRD, adr)
  
**CI**:
-   Github Actions configurado
-   Pipeline rodando `black --check` e `flake8` a cada push

## Decisões tomadas nesta sprint

| Decisão        | Escolha | Motivo                                                                            |
| -------------- | ------- | --------------------------------------------------------------------------------- |
| Banco de dados | SQLite  | Zero dependência de infra. Troca por Postgres exige mudar só a string de conexão. |
| Provedor de IA | Gemini  | Único com free tier disponível no momento.                                        |


> ADRs detalhados ficam em `docs/adr/`.

---

## Checklist

- [ ] Repositório criado e clonado localmente
- [ ] Estrutura de diretórios criada
- [ ] `.env` configurado com a Gemini API key
- [ ] `docker compose up` sobe backend e frontend sem erros
- [ ] `GET /health` retorna `{"status": "ok", "database": "ok"}`
- [ ] `GET /docs` exibe o Swagger UI gerado pelo FastAPI
- [ ] Frontend abre no browser sem erros no console
- [ ] Primeiro push no GitHub dispara o CI e passa

---

**Próxima sprint:** Sprint 1 — CRUD de recursos (backend + frontend)