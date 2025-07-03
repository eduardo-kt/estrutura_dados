"""
src/tabela_hash/main.py

# Lista Encadeada
class Elemento:
    # construtor de inicialização da classe
    def __init__(self, uf, nome_unidade):
        self.uf = uf
        self.nome_unidade = nome_unidade
        self.proximo = None

    # __repr__ é um método especial do Python
    # use-o para criar a maneira como objeto
    # é mostrado fora da função print
    def __repr__(self):
        return f"{self.nome_unidade}({self.uf})"


# Cria a lista encadeada simples
class ListaEncadeada:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodo = self.head
        nodos = []
        while nodo is not None:
            nodos.append(f"[{nodo.uf},{nodo.nome_unidade}]")
            nodo = nodo.proximo
        nodos.append("None")
        return " -> ".join(nodos)

    # Varre a lista
    def __iter__(self):
        nodo = self.head
        while nodo is not None:
            yield nodo
            nodo = nodo.proximo

    def inserir_no_inicio(self, nodo):
        nodo.proximo = self.head
        self.head = nodo


def msg_customizada(titulo):
    print("\n" + "=" * len(titulo))
    print(titulo)
    print("=" * len(titulo) + "\n")


def hash_func(k, n):
    return k % n


def hash_func_sigla(k, n):
    if k.upper() == "DF":
        return 7
    return (ord(k[0]) + ord(k[1])) % n


def imprimir_hash(tabela_hash):
    for i, lista in enumerate(tabela_hash):
        print(f"{i}: {lista}")


