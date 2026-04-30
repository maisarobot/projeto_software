# Documentação Funcional — FlowChat

**Sistema:** FlowChat  
**Aluna:** Maisa Barbosa Bispo  
**Tipo:** Aplicação de chat em terminal  
**Linguagem:** Python  
**Projeto base:** Inspirado no WhatsApp  

---

## Sumário

1. Menção Coletiva em Grupo  
2. Autenticação com Email  
3. Chat Individual  
4. Chat em Grupo  
5. Mensagens Fixadas  
6. Eventos  
7. Enquetes  
8. Busca de Mensagens  
9. Mensagem Temporária  
10. Reações em Mensagens  

---

## 1. Menção Coletiva em Grupo

**Classe:** `Grupo`

### Objetivo

Permitir notificar todos os membros de um grupo por meio da menção `@todos`, simulando o comportamento de aplicativos como WhatsApp.

### Funcionamento

Quando uma mensagem contém `@todos`, o método `mencionar_todos()` incrementa o contador de notificações de todos os membros do grupo, exceto o remetente.

### Entradas

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `conteudo` | `str` | Mensagem enviada contendo `@todos` |

### Saídas

| Resultado | Tipo | Descrição |
|---|---|---|
| Notificações | `int` | Quantidade de notificações por usuário |

### Regras

- O remetente não recebe notificação.
- As notificações são armazenadas por e-mail.
- As notificações são zeradas ao abrir o grupo.

---

## 2. Autenticação com Email

**Classes:** `Usuario`, `FlowChat`

### Objetivo

Permitir cadastro e login de usuários utilizando e-mail e senha.

### Funcionamento

- Cadastro: `cadastrar_usuario()` cria um novo usuário se o e-mail não existir.
- Login: `login()` valida as credenciais.

### Entradas

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `email` | `str` | E-mail do usuário |
| `senha` | `str` | Senha de acesso |

### Saídas

| Resultado | Tipo | Descrição |
|---|---|---|
| `True` | `bool` | Operação bem-sucedida |
| `False` | `bool` | Falha na operação |

### Regras

- Não permite e-mails duplicados.
- Login só ocorre com credenciais válidas.

---

## 3. Chat Individual

**Classe:** `ChatIndividual`

### Objetivo

Permitir comunicação privada entre dois usuários.

### Funcionamento

O sistema verifica se já existe um chat entre os usuários. Caso não exista, cria um novo.

### Entradas

| Parâmetro | Tipo |
|---|---|
| `usuario1` | `Usuario` |
| `usuario2` | `Usuario` |

### Saídas

| Resultado | Tipo |
|---|---|
| `ChatIndividual` | objeto |

### Regras

- Apenas dois usuários participam.
- Não é permitido chat consigo mesmo.

---

## 4. Chat em Grupo

**Classe:** `Grupo`

### Objetivo

Permitir comunicação entre múltiplos usuários.

### Funcionamento

O grupo é criado com um nome e lista de participantes. O criador é incluído automaticamente.

### Entradas

| Parâmetro | Tipo |
|---|---|
| `nome` | `str` |
| `emails` | `list` |

### Saídas

| Resultado | Tipo |
|---|---|
| `Grupo` | objeto |

### Regras

- Nome não pode ser vazio.
- Nome deve ser único.
- Todos os usuários devem existir.

---

## 5. Mensagens Fixadas

**Classes:** `Mensagem`, `Chat`

### Objetivo

Destacar mensagens importantes no topo do chat.

### Funcionamento

O método `fixar_mensagem()` move a mensagem para o início da lista e marca como fixada.

### Entradas

| Parâmetro | Tipo |
|---|---|
| `indice` | `int` |

### Saídas

| Resultado | Tipo |
|---|---|
| `True` | `bool` |
| `False` | `bool` |

### Regras

- Apenas mensagens existentes podem ser fixadas.
- Mensagem recebe o marcador `[FIXADA]`.

---

## 6. Eventos

**Classe:** `Evento`

### Objetivo

Permitir criação e gerenciamento de eventos dentro do chat.

### Funcionamento

Eventos possuem nome, data, descrição e organizador. Podem ser editados ou cancelados.

### Entradas

| Parâmetro | Tipo |
|---|---|
| `nome` | `str` |
| `data` | `str` |
| `descricao` | `str` |
| `organizador` | `Usuario` |

### Saídas

| Resultado | Tipo |
|---|---|
| `Evento` | objeto |
| `True/False` | bool |

### Regras

- Apenas o organizador pode editar ou cancelar.
- Status inicial: `programado`.

---

## 7. Enquetes

**Classe:** `Enquete`

### Objetivo

Permitir criação de votações dentro dos chats.

### Funcionamento

Os votos são armazenados em um dicionário usando o e-mail do usuário como chave.

### Entradas

| Parâmetro | Tipo |
|---|---|
| `pergunta` | `str` |
| `usuario` | `Usuario` |
| `opcao` | `str` |

### Saídas

| Resultado | Tipo |
|---|---|
| `dict` | votos |

### Regras

- Um usuário possui apenas um voto (substituível).
- Pergunta e voto não podem ser vazios.

---

## 8. Busca de Mensagens

**Classe:** `Chat`

### Objetivo

Permitir encontrar mensagens por palavra-chave.

### Funcionamento

O método `pesquisar_mensagens()` filtra mensagens que contêm o termo buscado.

### Entradas

| Parâmetro | Tipo |
|---|---|
| `termo` | `str` |

### Saídas

| Resultado | Tipo |
|---|---|
| `list` | mensagens encontradas |

### Regras

- A busca não diferencia maiúsculas de minúsculas.
- Apenas mensagens não expiradas são consideradas.

---

## 9. Mensagem Temporária

**Classes:** `Mensagem`, `Chat`

### Objetivo

Permitir envio de mensagens que desaparecem automaticamente.

### Funcionamento

A mensagem recebe um tempo de expiração e é removida após esse tempo.

### Entradas

| Parâmetro | Tipo |
|---|---|
| `mensagem` | `Mensagem` |
| `segundos` | `int` |

### Saídas

| Resultado | Tipo |
|---|---|
| Lista atualizada | `list` |

### Regras

- Tempo padrão: 5 segundos.
- Mensagens expiradas não são exibidas.

---

## 10. Reações em Mensagens

**Classes:** `Mensagem`, `Chat`

### Objetivo

Permitir interação com mensagens por meio de emojis.

### Funcionamento

As reações são armazenadas na lista `reacoes` da mensagem.

### Entradas

| Parâmetro | Tipo |
|---|---|
| `indice` | `int` |
| `reacao` | `str` |

### Saídas

| Resultado | Tipo |
|---|---|
| `True/False` | bool |

### Regras

- Só é possível reagir a mensagens existentes.
- Reações são acumulativas.

---

## Considerações Finais

O **FlowChat**, é um sistema inspirado no WhatsApp que simula funcionalidades essenciais de comunicação em um ambiente de terminal.

O projeto utiliza conceitos de Programação Orientada a Objetos e apresenta uma estrutura modular, facilitando manutenção e expansão futura.
