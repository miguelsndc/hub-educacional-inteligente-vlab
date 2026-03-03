# Sprint 2 — Frontend + Smart Assist

**Objetivo:** Interface completa integrada com o backend, incluindo o Smart Assist com Gemini.  
**Estimativa:** 6–8 horas.  
**Definição de pronto:** É possível realizar todas as operações do CRUD pela interface, e o botão de IA preenche descrição e tags automaticamente.

---

## O que precisa existir ao final dessa sprint

**Configuração:**
- Projeto Vite + React + TypeScript inicializado
- TailwindCSS configurado
- React Query, Axios e React Router instalados

**Parte de serviços:**
- Instância do Axios com tratamento de erro centralizado
- Funções tipadas para cada operação do CRUD
- Função para chamar o endpoint do Smart Assist

**Hooks:**
- Listagem paginada com React Query
- Mutations para criação, edição e exclusão com invalidação de cache
- Hook dedicado para o fluxo de assistência inteligente

**Componentes:**
- Primitivos de formulário reutilizáveis (input, select, textarea, label)
- Input de tags como chips interativos
- Modal de confirmação de exclusão
- Controle de paginação
- Tabela de recursos com ações
- Formulário unificado para criação e edição com assist

**Páginas:**
- Listagem com paginação
- Formulário de criação e edição
- Página especifica do recurso

**Smart Assist:**
- Botão disponível apenas quando título e tipo estão preenchidos
- Loading com mensagem textual durante a chamada
- Preenchimento automático de descrição e tags em caso de sucesso
- Mensagem de erro sem corromper o formulário em caso de falha

---

## Decisões tomadas nesta sprint

| Decisão                     | Escolha                            | Motivo                                                    |
| --------------------------- | ---------------------------------- | --------------------------------------------------------- |
| Gerenciamento de formulário | Estado local com `useState`        | Sem necessidade de biblioteca externa para o escopo atual |
| Criação e edição            | Componente de formulário unificado | Evita duplicação de lógica e UI                           |
| Componentes de formulário   | Primitivos próprios                | Consistência visual sem dependência de biblioteca de UI   |

---

## Checklist

- [x] Frontend sobe via Docker sem erros
- [x] Listagem exibe recursos e pagina corretamente
- [x] Criação salva e redireciona para listagem
- [x] Edição pré-preenche o formulário corretamente
- [x] Exclusão exige confirmação e remove da listagem
- [x] Tags adicionadas e removidas individualmente
- [x] Botão de IA desabilitado sem título e tipo preenchidos
- [x] Smart Assist preenche descrição e tags automaticamente
- [x] Erro da IA exibe mensagem sem quebrar o formulário
- [ ] CI passa após o push

---

**Próxima sprint:** Sprint 3 — Polimento e entrega