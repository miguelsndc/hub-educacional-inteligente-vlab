## PRD - Hub Inteligente de Recursos Educacionais

**Versão**: 1.0

**Autor**: Miguel Nogueira


## Problema

A equipe de materiais digitais mantém um reposotório descentralizado de recursos educacionais. O processo de catalogação atual é manual, lento e inconsistente: conteudistas diferentes descrevem materiais similares de formas incompatíveis, dificultando busca, reuso e manutenção do acervo.

## Objetivo

Centralizar o gerenciamento de recursos didáticos em uma única plataforma e reduzir o tempo de catalogação através de sugestões geradas por I.A, mas mantendo o conteudista no controle da decisão final

## Personas

**Conteudista**: Responsável por cadastrar e manter os recursos educacionais. Quer velocidade no preenchimento e consistência nas descrições entre diferentes materiais

## Features

**F1 - Listagem de Recursos**:
Exibir todos os recursos cadastrados em uma tabela paginada, com as informações essenciais visíveis e ações de edição e exclusão acessíveis diretamente na listagem.

Campos exibidos: *título, tipo, tags, data de criação*

Paginação: *lado do servidor, 10 itens por página como padrão*

**F2 - Cadastro de Recurso**:
Formulário para criação de novos recursos com validação no lado do cliente e do servidors. Tags devem ser gerenciadas como componentes individuais, não como campo de texto livre.

Campos: *Título (obrigatório), Descrição, Tipo (obrigatório), URL, Tags*

**F3 - Edição de Recurso**:
Formulário idêntico ao de cadastro, pré-preenchido com os dados existentes. O Smart Assist deve estar disponível também na edição, permitindo regeração das sugestões.

**F4 - xclusão de Recurso**:
Exclusão com confirmação obrigatória via modal. Feedback visual após a operação.

**F5 - Smart Assist**:
Um assistente pedagógico baseado em IA que sugere descrição e tags a partir do título e do tipo do recurso, reduzindo o esforço de catalogação e aumentando a consistência do acervo.

O preenchimento automático é uma sugestão. O conteudista pode editar livremente antes de salvar.

Comportamento esperado:

1.  Botão disponível apenas quando Título e Tipo estiverem preenchidos
2.  Loading state com feedback textual durante a chamada

    **Em sucesso:** campos preenchidos, foco movido para descrição

    **Em falha:** mensagem contextual, formulário intacto


**Fora do Escopo (v1)**
Os itens abaixo foram conscientemente excluídos desta versão para manter o foco no fluxo principal.

-   Autenticação e controle de acesso
    
-   Busca e filtro por texto ou tags
-   Upload de arquivos
-   Preview de URLs
-   Histórico de edições
-   Ordenação da listagem


## Critérios de Aceitação

**F1 - Listagem**

 Recursos exibidos em tabela com paginação funcional

 Navegação entre páginas sem recarregar a página

 Estado vazio com mensagem orientativa quando não há recursos

**F2 F3 Formulário**

 Campos obrigatórios bloqueiam envio se vazios

 Erros de validação exibidos inline, por campo

 Tags adicionadas e removidas individualmente

 Feedback de sucesso após salvar

**F4 Exclusão**

 Modal de confirmação antes de deletar

 Recurso removido da listagem imediatamente após confirmação

 Ação cancelável

**F5 Smart Assist**

 Botão desabilitado se Título ou Tipo ausentes

 Loading state visível durante a requisição

 Campos preenchidos automaticamente em caso de sucesso

 Campos permanecem editáveis após o 
 preenchimento

 Falha de rede exibe mensagem sem corromper o formulário
 
 Timeout de 30s com mensagem específica