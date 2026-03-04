# Hub Inteligente de Recursos Educacionais

**Desafio Técnico VLAB** - Plataforma fullstack para catalogação de materiais didáticos com assistência de IA para geração automática de descrições e tags.

---

## Sobre o projeto

A equipe de Materiais Digitais precisava de um repositório centralizado para recursos educacionais. O processo de catalogação manual era lento e gerava inconsistências. Conteudistas diferentes descreviam materiais similares de formas incompatíveis, dificultando a busca e o reuso.

Esta plataforma resolve esse problema centralizando o gerenciamento e reduzindo o esforço de catalogação através de **Assistência Inteligente**, um auxílio pedagógico baseado em IA que sugere descrições e tags a partir do título e tipo do material. O conteudista permanece no controle: as sugestões são editáveis antes de salvar, e o fluxo de catalogação nunca depende exclusivamente da IA para funcionar.

---

## Stack de Desenvolvimento

| Camada   | Tecnologias                                                   |
| -------- | ------------------------------------------------------------- |
| Backend  | Python 3.12 · FastAPI · SQLAlchemy 2.0 · SQLite · Pydantic v2 |
| Frontend | React · TypeScript · Vite · TailwindCSS · React Query · Axios |
| IA       | Google Gemini Flash                                           |
| Infra    | Docker · Docker Compose · GitHub Actions                      |

---
DISCLAIMER: *por algum motivo que desconheço, ao especificar uma versão do flash como 2.0 ou 1.5, a api me rejeitava com 429 - quota exceeded, porém, ao colocar o modelo como gemini-flash-latest, funciona sem problemas.*

## Arquitetura

O projeto é dividido em três camadas principais: backend, frontend e documentação. O backend expõe uma API REST consumida pelo frontend, e a comunicação com a IA acontece inteiramente no backend, ou seja, o frontend nunca toca na API do Gemini diretamente.

```
hub-recursos-educacionais/
├── backend/
│   ├── app/
│   │   ├── models/          # Models SQLAlchemy (Resource, Tag)
│   │   ├── schemas/         # Schemas Pydantic de entrada e saída
│   │   ├── services/        # Regras de negócio (resource_service, ai_service)
│   │   ├── routers/         # Endpoints FastAPI (resources, ai, health)
│   │   ├── providers/       # Provedores de IA (Gemini, Mock, protocolo)
│   │   ├── prompts/         # Prompts de sistema para a IA
│   │   ├── main.py          # Inicialização da aplicação
│   │   ├── database.py      # Engine, sessão e Base do SQLAlchemy
│   │   ├── settings.py      # Configurações centralizadas via pydantic-settings
│   │   ├── seeder.py        # Script de seed para popular o banco de dados
│   │   ├── constants.py     # Constantes e enums do projeto
│   │   ├── exceptions.py    # Hierarquia de exceções customizadas
│   │   └── logger.py        # Logger estruturado em JSON
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/      # Componentes reutilizáveis
│   │   ├── pages/           # ListPage e FormPage
│   │   ├── hooks/           # Hooks de dados e UI
│   │   └── services/        # Chamadas à API (resources, ai, axios)
│   ├── Dockerfile
│   └── .env.example
├── docs/
│   ├── adr/                 # Architecture Decision Records
│   ├── requisitos.md        # Requisitos do produto
│   ├── sprints/             # Planejamento de sprints
│   └── divida-técnica.md    # Dívidas técnicas conhecidas
├── .github/
│   └── workflows/
│       └── ci.yml           # Pipeline de lint
└── docker-compose.yml
```

No backend, a separação entre `models`, `schemas` e `services` traz independência: os models pertencem ao SQLAlchemy e representam o estado do banco, os schemas pertencem ao Pydantic e representam os dados que entram e saem da API, e os services contêm as regras de negócio sem depender de nenhum dos dois diretamente. Essa separação evita que uma mudança no banco quebre a API ou vice-versa.

No frontend, a camada de `services` centraliza todas as chamadas HTTP: nenhum componente faz requisições diretamente. Os `hooks` encapsulam o estado assíncrono com React Query, deixando os componentes responsáveis apenas por renderização, e a biblioteca lida com erros, loading e cache automaticamente.

---

## Decisões de arquitetura

### SQLite como banco de dados

A escolha do SQLite elimina qualquer dependência de infraestrutura externa para rodar o projeto. Para avaliação e desenvolvimento, isso significa que basta clonar o repositório e seguir o README, então nenhum banco precisa ser provisionado. A decisão não compromete uma migração futura: o SQLAlchemy abstrai o banco através da variavel de ambiente `DATABASE_URL`, e trocar para PostgreSQL em produção exige apenas mudar uma linha no `.env`.

### Tags como entidade própria

A abordagem mais simples seria armazenar tags como um campo JSON dentro do recurso. Essa opção foi descartada porque inviabiliza busca por tag, impede reuso entre recursos e abre espaço para inconsistências de vocabulário. Em vez disso, tags vivem em uma tabela própria com um relacionamento many-to-many com recursos. Toda tag é normalizada antes de ser salva, convertida para snake-case, o que garante que "Python", "python" e " python " sejam tratadas como a mesma tag.

### Provider pattern para IA

A integração com o Gemini não está espalhada pelo código — ela fica encapsulada dentro de `providers/gemini.py`, que implementa um protocolo comum `AIProvider`. A factory em `providers/factory.py` lê a variável `AI_PROVIDER` do `.env` e instancia o provider correto. Isso significa que adicionar suporte a um novo provedor de IA é uma questão de criar um novo arquivo que implemente o protocolo, sem tocar em nenhum outro código. Durante o desenvolvimento, o `MockProvider` permite trabalhar sem consumir a API do Gemini.

### Logs estruturados em JSON

Em vez de logs em texto livre, todos os eventos seguem um formato JSON consistente. Isso facilita filtragem, indexação e integração com ferramentas de observabilidade. Campos de contexto são adicionados via prefixo `ctx_`, o formatador remove o prefixo na serialização. Cada chamada ao Smart Assist gera um log com título, latência e tokens consumidos:

```json
{
  "timestamp": "2026-03-03T22:11:23.532131+00:00",
  "level": "INFO",
  "message": "AI Request",
  "logger": "app.providers.gemini",
  "title": "Matemática Financeira",
  "latency": 1.43,
  "token_usage": 187
}
```

> As decisões detalhadas, incluindo as alternativas consideradas e os motivos pelos quais foram descartadas, estão documentadas em `docs/adr/`.

---

## Como rodar o projeto localmente
### Pré requisitos

**Com Docker (recomendado):**
- Docker e Docker Compose instalados

**Sem Docker:**
- Python 3.11+
- Node.js 18+

**Em ambos os casos:**
- Chave de API do Google Gemini — obtenha gratuitamente em [aistudio.google.com](https://aistudio.google.com/app/apikey)

---

### Instalação e execução

**Com Docker**

A forma mais simples de rodar o projeto. O Docker Compose sobe o backend e o frontend em containers isolados com hot reload habilitado.

```bash
git clone https://github.com/seu-usuario/hub-recursos-educacionais.git
cd hub-recursos-educacionais

# Configurar variáveis de ambiente
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Editar backend/.env e adicionar a GEMINI_API_KEY
```

```bash
docker compose up --build
```

**Sem Docker**


**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# Editar .env e adicionar a GEMINI_API_KEY

uvicorn app.main:app --reload
```

**Frontend** (em outro terminal):
```bash
cd frontend
npm install

cp .env.example .env

npm run dev
```

### Popular o banco com dados de teste

Para facilitar a avaliação visual da interface, um seeder está disponível para criar 100 recursos de exemplo:

```bash
# Com Docker
docker compose exec backend python -m app.seeder

# Sem Docker (com venv ativo)
cd backend && python -m app.seeder
```

### Acessos

| Serviço                 | URL                          |
| ----------------------- | ---------------------------- |
| Frontend                | http://localhost:5173        |
| API                     | http://localhost:8000        |
| Documentação interativa | http://localhost:8000/docs   |
| Health check            | http://localhost:8000/health |

---

## Variáveis de ambiente

### Backend (`backend/.env`)

| Variável             | Descrição                                             | Padrão                  |
| -------------------- | ----------------------------------------------------- | ----------------------- |
| `DATABASE_URL`       | String de conexão com o banco                         | `sqlite:///./app.db`    |
| `AI_PROVIDER`        | Provider de IA ativo: `gemini`, `anthropic` ou `mock` | `gemini`                |
| `GEMINI_API_KEY`     | Chave da API do Gemini                                | —                       |
| `GEMINI_MODEL`       | Modelo do Gemini a utilizar                           | `gemini-flash-latest`   |
| `AI_TIMEOUT_SECONDS` | Timeout das chamadas à IA em segundos                 | `30`                    |
| `ENVIRONMENT`        | Ambiente de execução                                  | `development`           |
| `CORS_ORIGINS`       | Origens permitidas para CORS                          | `http://localhost:5173` |

> Para rodar sem depender da API do Gemini, defina `AI_PROVIDER=mock`. O Smart Assist retornará uma resposta fixa, mas todo o restante da aplicação funcionará normalmente.

### Frontend (`frontend/.env`)

| Variável       | Descrição                  | Padrão                  |
| -------------- | -------------------------- | ----------------------- |
| `VITE_API_URL` | URL base da API do backend | `http://localhost:8000` |

---

## Endpoints da API

| Método   | Endpoint          | Descrição                                 |
| -------- | ----------------- | ----------------------------------------- |
| `GET`    | `/health`         | Health check — verifica API e banco       |
| `GET`    | `/resources`      | Listagem paginada (`?page=1&limit=10`)    |
| `POST`   | `/resources`      | Criar recurso                             |
| `GET`    | `/resources/{id}` | Detalhe de um recurso                     |
| `PUT`    | `/resources/{id}` | Atualizar recurso                         |
| `DELETE` | `/resources/{id}` | Excluir recurso                           |
| `POST`   | `/ai/suggest`     | Gerar sugestão de descrição e tags com IA |

A documentação interativa completa, com schemas de entrada e saída e possibilidade de testar os endpoints diretamente no browser, está disponível em `/docs` após subir o backend.

---

## Assistência Inteligente

O botão **Gerar Descrição com IA** fica disponível no formulário de criação e edição assim que título e tipo estiverem preenchidos e esses dois campos são suficientes para a IA gerar uma sugestão útil.

Ao clicar, o frontend envia o título e o tipo para o endpoint `/ai/suggest`. O backend carrega as tags já existentes no banco e monta uma mensagem para o Gemini que inclui essas informações. O prompt de sistema instrui a IA a atuar como Assistente Pedagógico: gerar uma descrição objetiva em português, focada no benefício para o aluno, e sugerir três tags relevantes priorizando o vocabulário já existente. Isso evita que o banco acumule tags semanticamente equivalentes escritas de formas diferentes.

A resposta da IA é validada antes de retornar ao frontend. Se o formato for inesperado (o que pode acontecer, dado que LLM's são por várias vezes imprevisíveis), um erro descritivo é retornado e o formulário permanece intacto. O conteudista pode tentar novamente ou preencher os campos manualmente.

Cada interação com a Assistência Inteligente gera um log estruturado com título, latência e tokens consumidos, facilitando monitoramento de uso e custo.

---

## Documentação

A pasta `docs/` reúne toda a documentação de produto e decisões técnicas do projeto.

| Documento                        | Descrição                                                          |
| -------------------------------- | ------------------------------------------------------------------ |
| `docs/requisitos.md`             | Requisitos do produto, personas e critérios de aceite              |
| `docs/adr/001_banco-de-dados.md` | Por que SQLite e como migrar para PostgreSQL                       |
| `docs/adr/002_tags.md`           | Por que many-to-many, normalização e fluxo de aprovação descartado |
| `docs/divida-técnica.md`         | Dívidas técnicas conhecidas e melhorias futuras                    |

Os ADRs (Architecture Decision Records) documentam não só a decisão tomada, mas as alternativas consideradas e os motivos pelos quais foram descartadas. São úteis para entender o raciocínio por trás das escolhas sem precisar ler o código.

---

## Próximos passos

- Autenticação e controle de acesso por perfil de usuário
- Busca e filtro por título e tags
- Fluxo de aprovação de novas tags sugeridas pela IA, evitando proliferação de sinônimos
- Modo de complemento no Smart Assist — completar a descrição existente ao invés de substituí-la
- Migração para PostgreSQL para ambientes de produção
- Testes automatizados nas partes críticas do sistema