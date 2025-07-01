# src/lista_encadeada/componentes/lista.py


class Cartao:
    def __init__(self, cor, nro):
        self.cor = cor
        self.nro = nro

    def __repr__(self):
        return f"{self.cor}{self.nro}"


class Elemento:
    def __init__(self, cartao):
        self.dado = cartao
        self.proximo = None

    def __repr__(self):
        return repr(self.dado)


class ListaHospitalar:
    def __init__(self, nodos=None):
        self.head = None
        if nodos is not None:
            nodo = Elemento(nodos.pop(0))
            self.head = nodo
            for item in nodos:
                nodo.proximo = Elemento(item)
                nodo = nodo.proximo

    def __repr__(self):
        nodo = self.head
        nodos = []
        while nodo is not None:
            nodos.append(repr(nodo.dado))
            nodo = nodo.proximo
        nodos.append("None")
        return " -> ".join(nodos)

    def __iter__(self):
        nodo = self.head
        while nodo is not None:
            yield nodo
            nodo = nodo.proximo

    def inserirNoInicio(self, nodo: Elemento):
        nodo.proximo = self.head
        self.head = nodo

    def inserirNoFinal(self, nodo: Elemento):
        if self.head is None:
            self.head = nodo
            return

        nodo_atual = self.head
        while nodo_atual.proximo is not None:
            nodo_atual = nodo_atual.proximo

        nodo_atual.proximo = nodo

    def deletar(self, cartao):
        if self.head is None:
            raise Exception("Lista vazia")
        # fmt: off
        if (
            self.head.dado.nro == cartao.nro
            and self.head.dado.cor == cartao.cor
        ):
            self.head = self.head.proximo
            return

        nodo_anterior = self.head
        for nodo in self:
            if nodo.dado.nro == cartao.nro and nodo.dado.cor == cartao.cor:
                nodo_anterior.proximo = nodo.proximo
                return
            nodo_anterior = nodo

        raise Exception(f"Nó com o cartão '{cartao}' não foi encontrado")


if __name__ == "__main__":
    # Criando cartões
    c1 = Cartao("V", 7)
    c2 = Cartao("V", 15)
    c3 = Cartao("V", 4)
    c4 = Cartao("A", 240)
    c5 = Cartao("A", 212)
    c6 = Cartao("V", 64)
    c7 = Cartao("V", 114)

    Teste = ListaHospitalar()

    # Inserções no início (ordem inversa na lista final)
    Teste.inserirNoInicio(Elemento(c4))
    Teste.inserirNoInicio(Elemento(c3))
    Teste.inserirNoInicio(Elemento(c2))
    Teste.inserirNoInicio(Elemento(c1))
    Teste.inserirNoInicio(Elemento(c7))

    # Inserções no final
    Teste.inserirNoFinal(Elemento(c5))
    Teste.inserirNoFinal(Elemento(c6))

    print("Lista completa:")
    print(Teste)

    Teste.deletar(c3)

    print("\nApos atender o cartao %s:" % c3)
    print(Teste)
