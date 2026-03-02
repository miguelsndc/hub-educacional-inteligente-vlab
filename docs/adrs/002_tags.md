# ADR-002 — Modelagem e estratégia de tags

**Status:** Aceito  
**Data:** 01/03/2026

---

## Contexto

O sistema precisa associar as tags aos recursos educacionais. como modelar essa relação tem impacto direto na qualidade dos dados, na capacidade de busca futura e na integração com a assistência inteligente

## Opções consideradas

**Tags como JSON no modelo de recurso**
A abordagem mais simples: armazenar tags como uma lista json diretamente na tabela de recursos. Sem relacionamento, sem tabela extra

Problema: impossibilita busca por tag, não permite reuso entre recursos e abre espaço para inconsistências tipo "machine-learning", "Machine Learning" e "ml" serem tratadas como tags diferentes

**Tags como entidade própria com relacionamento many-to-many**
Tabela `tags` independente, vinculada aos recursos através de uma tabela de junção como `resource_tags`. Uma tag pode pertencer a vários recursos e um recurso pode ter várias tags

Permite busca por tag, reuso entre recursos e controle sobre o vocabulário existente

**Tags globais com aprovação de novas sugestões da IA**
Extensão da opção anterior: a IA recebe no prompt a lista de tags ativas e prioriza reutilizá-las. Quando nenhuma tag existente for adequada, a IA pode sugerir novas, que ficam com status pendente até aprovação humana durante a criação do recurso, as tags *devem* ser aprovadas antes da adição do novo recurso à base de dados.

Isso resolve o problema de proliferação de tags semanticamente equivalentes, mas adiciona a complexidade de fluxo: novo status, tela de aprovação, lógica de vinculação pós-aprovação.

## Decisão

Many-to-many com normalização, sem fluxo de aprovação nesta versão.

Tags são armazenadas em tabela própria e vinculadas ao recursos via uma tabela de junção. Toda tag é normalizada antes de ser salva (convertemos para snake-case), para evitar duplicatas por variação de capitalização ou espaços.

O fluxo de aprovação de novas tags sugeridas pela IA foi descartado para esta versão por estar *fora do escopo do desafio* e consumir tempo incompatível com o prazo de entrega.

## Consequências

A normalização resolve a inconsistência mais comum, mas não impede sinônimos ("ml" e "machine-learning" coexistiriam como tags distintas). Isso seria endereçado pelo fluxo de aprovação, deixado como evolução planejada.

## Evolução planejada (v2)

Adicionar campo `status` na tabela `tags` com valores `active` e `pending`. A IA passaria a receber no prompt a lista de tags ativas e priorizaria reutilizá-las. Sugestões fora do vocabulário existente entrariam como `pending`, visíveis para aprovação antes de serem incorporadas ao acervo.