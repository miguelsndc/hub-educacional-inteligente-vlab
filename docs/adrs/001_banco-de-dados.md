# ADR-001 SQLite como Banco de Dados

**Status:** Aceito

**Data:** 28/02/2026

## Contexto

O desafio permite MySQL, PostgreSQL ou SQLite. A escolha impacta diretamente quem for avaliar o projeto: quanto mais dependências externas, maior a chance de falhar na hora de rodar localmente.

## Decisão

SQLite para desenvolvimento e entrega.

## Justificativa

Elimina qualquer dependência de infra externa. Quem clonar o repositório não precisa instalar ou configurar nenhum banco, ele é criado automaticamente na primeira execução.

A camada do SQLAlchemy abstrai o banco completamente. Migrar para PostgreSQL em produção exige apenas mudar o valor de `DATABASE_URL` no `.env`, sem tocar em nenhuma linha de código da aplicação.

## Consequências

SQLite não suporta múltiplas operações de escrita de modo concorrente, e é de modo geral uma opção com performance inferior e requer gerenciamento manual. Isso é **irrelevante** pro escopo atual, mas seria **o primeiro item** a endereçar em uma evolução para produção.
