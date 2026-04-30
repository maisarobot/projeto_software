# Herança no Sistema FlowChat

**Sistema:** FlowChat  
**Aluna:** Maisa Barbosa Bispo  
**Projeto base:** Inspirado no WhatsApp  

---

## Conceito de Herança

A herança é um conceito da Programação Orientada a Objetos que permite que uma classe reutilize atributos e métodos de outra classe.

Uma classe filha herda comportamentos da classe pai, podendo:
- reutilizar código existente  
- adicionar novos atributos e métodos  
- modificar comportamentos herdados  

Em Python, a herança é definida assim:

```python
class ClasseFilha(ClassePai):
    pass
```

---

## Uso da Herança no FlowChat

No sistema **FlowChat**, a herança foi utilizada para organizar o código e evitar repetição.

Foram utilizadas duas principais hierarquias:

---

## 1. Chat → ChatIndividual e Grupo

### Código

```python
class Chat:
    def __init__(self):
        self.mensagens = []
        self.enquetes = []
        self.eventos = []

class ChatIndividual(Chat):
    def __init__(self, usuario1, usuario2):
        super().__init__()
        self.usuario1 = usuario1
        self.usuario2 = usuario2

class Grupo(Chat):
    def __init__(self, nome=None):
        super().__init__()
        self.nome = nome
        self.membros = []
        self.notificacoes = {}
```

### Motivo da herança

Chats individuais e grupos possuem várias funcionalidades em comum:
- armazenamento de mensagens  
- criação de enquetes  
- criação de eventos  
- busca de mensagens  
- reações e fixação  

A classe `Chat` centraliza essas funcionalidades, evitando duplicação.

### O que é herdado

- `mensagens`  
- `enquetes`  
- `eventos`  
- métodos como envio, busca, reações e fixação  

### O que cada classe adiciona

| Classe | Adições |
|---|---|
| `ChatIndividual` | usuários do chat |
| `Grupo` | membros e notificações |

---

## 2. Mensagem → MensagemPrivada e MensagemGrupo

### Código

```python
class Mensagem:
    def __init__(self, remetente, conteudo):
        self.remetente = remetente
        self.conteudo = conteudo
        self.reacoes = []
        self.fixada = False

class MensagemPrivada(Mensagem):
    def __init__(self, remetente, conteudo):
        super().__init__(remetente, conteudo)
        self.visualizada = False

class MensagemGrupo(Mensagem):
    def __init__(self, remetente, conteudo):
        super().__init__(remetente, conteudo)
        self.lida_por = []
```

### Motivo da herança

Todas as mensagens possuem características comuns:
- remetente  
- conteúdo  
- reações  
- estado de fixação  

A classe `Mensagem` define essa base.

As subclasses adicionam comportamentos específicos.

### O que é herdado

- `remetente`  
- `conteudo`  
- `reacoes`  
- `fixada`  

### O que cada classe adiciona

| Classe | Atributo extra |
|---|---|
| `MensagemPrivada` | `visualizada` |
| `MensagemGrupo` | `lida_por` |

---

## 3. Reaproveitamento de Métodos

A herança também permite reutilizar métodos definidos na classe `Chat`.

### Exemplo

```python
def pesquisar_mensagens(self, termo):
    return [m for m in self.mensagens if termo.lower() in m.conteudo.lower()]
```

Esse método funciona automaticamente para:
- chats individuais  
- grupos  

---

## Conclusão

No sistema **FlowChat**, a herança foi utilizada para:

- evitar repetição de código  
- centralizar funcionalidades comuns  
- facilitar manutenção  
- permitir expansão do sistema  

---

**Aluna:** Maisa Barbosa Bispo
