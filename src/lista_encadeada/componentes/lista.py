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
        self.contador_V = 1
        self.contador_A = 201
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

    def imprimirListaEspera(self):
        contador = 1
        if self.head is None:
            print("\nLista de espera vazia.")
            return
        print("\nLista de Espera:")
        for nodo in self:
            print(f"{contador}: {nodo.dado.cor}{nodo.dado.nro}")
            contador += 1

    def __iter__(self):
        nodo = self.head
        while nodo is not None:
            yield nodo
            nodo = nodo.proximo

    def inserir(self):
        cor = (
            input(
                """
    Digite:
    A - Amarelo (Prioridade)
    V - Vermelho

    Informe a cor do cartao: """
            )
            .strip()
            .upper()
        )
        if cor == "V":
            nro = self.contador_V
            self.contador_V += 1

        elif cor == "A":
            nro = self.contador_A
            self.contador_A += 1
        else:
            print("Opcao Invalida. Retornando ao menu principal.")
            return

        cartao = Cartao(cor, nro)
        nodo = Elemento(cartao)

        if self.head is None:
            self.head = nodo
        elif cor == "V":
            self.inserirSemPrioridade(nodo)
        elif cor == "A":
            self.inserirComPrioridade(nodo)

    def inserirNoInicio(self, nodo: Elemento):
        nodo.proximo = self.head
        self.head = nodo

    def inserirSemPrioridade(self, nodo: Elemento):
        if self.head is None:
            self.head = nodo
            return

        nodo_atual = self.head
        while nodo_atual.proximo is not None:
            nodo_atual = nodo_atual.proximo

        nodo_atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
            return

        nodo_anterior = None
        nodo_atual = self.head

        while (
            nodo_atual is not None
            and nodo_atual.dado.cor == "A"
            and nodo_atual.dado.nro < nodo.dado.nro
        ):
            nodo_anterior = nodo_atual
            nodo_atual = nodo_atual.proximo

        if nodo_anterior is None:
            nodo.proximo = self.head
            self.head = nodo
        else:
            nodo.proximo = nodo_atual
            nodo_anterior.proximo = nodo

    def atenderPaciente(self):
        if self.head is None:
            print("Nenhum paciente em espera")
            return

        paciente_atendido = self.head.dado
        self.head = self.head.proximo

        print(
            f""""
Paciente {paciente_atendido.cor}{paciente_atendido.nro}.
Favor, dirija-se ao atendimento.
"""
        )


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
    Teste.inserirComPrioridade(Elemento(c4))
    Teste.inserirComPrioridade(Elemento(c3))
    Teste.inserirComPrioridade(Elemento(c2))
    Teste.inserirComPrioridade(Elemento(c1))
    Teste.inserirComPrioridade(Elemento(c7))

    # Inserções no final
    Teste.inserirSemPrioridade(Elemento(c5))
    Teste.inserirSemPrioridade(Elemento(c6))

    print("Lista completa:")
    print(Teste)

    Teste.deletar(c3)

    print("\nApos atender o cartao %s:" % c3)
    print(Teste)
