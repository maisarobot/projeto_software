# Polimorfismo no Sistema FlowChat

**Sistema:** FlowChat  
**Aluna:** Maisa Barbosa Bispo  
**Projeto base:** Inspirado no WhatsApp  

---

## O que é Polimorfismo?

O polimorfismo permite que um mesmo método seja chamado em objetos diferentes, produzindo comportamentos distintos dependendo do tipo do objeto.

Ou seja, o código pode chamar um método sem precisar saber exatamente qual classe está sendo utilizada.

---

## Aplicação no FlowChat

No sistema **FlowChat**, o polimorfismo aparece principalmente no comportamento das mensagens e dos chats.

---

## 1. exibir() — em Mensagem

```python
class Mensagem:
    def exibir(self, indice=None):
        prefixo = f"{indice} - " if indice is not None else ""
        fixada = "[FIXADA] " if self.fixada else ""
        print(f"{fixada}{prefixo}{self.remetente.email}: {self.conteudo}")
```

Uso:

```python
mensagem.exibir(i)
```

Mesmo sem saber o tipo da mensagem, o método funciona corretamente.

---

## 2. criar_mensagem() — ChatIndividual vs Grupo

```python
class ChatIndividual(Chat):
    def criar_mensagem(self, remetente, conteudo):
        return MensagemPrivada(remetente, conteudo)

class Grupo(Chat):
    def criar_mensagem(self, remetente, conteudo):
        return MensagemGrupo(remetente, conteudo)
```

Uso:

```python
mensagem = chat.criar_mensagem(usuario, conteudo)
```

O tipo da mensagem muda automaticamente conforme o tipo de chat.

---

## 3. titulo() — comportamento diferente

```python
class Chat:
    def titulo(self, usuario=None):
        return "Chat"

class ChatIndividual(Chat):
    def titulo(self, usuario=None):
        return f"Chat com {self.outro_usuario(usuario).email}"

class Grupo(Chat):
    def titulo(self, usuario=None):
        return f"Grupo: {self.nome}"
```

Uso:

```python
chat.titulo(usuario)
```

---

## 4. registrar_mensagem() — comportamento específico

```python
class Grupo(Chat):
    def registrar_mensagem(self, remetente, conteudo):
        mensagem = self.criar_mensagem(remetente, conteudo)
        self.enviar_mensagem(mensagem)

        if "@todos" in conteudo:
            self.mencionar_todos(remetente)

        return mensagem
```

---

## Conclusão

O polimorfismo no FlowChat permite:

- reutilizar métodos com comportamentos diferentes  
- evitar condicionais desnecessárias  
- facilitar expansão do sistema  

---

**Aluna:** Maisa Barbosa Bispo
