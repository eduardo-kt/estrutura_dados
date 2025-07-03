# src/lista_encadeada/main.py


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

    def imprimir_lista_espera(self):
        if self.head is None:
            print("Lista de espera vazia.")
            return
        lista_espera = []
        for nodo in self:
            lista_espera.append(f"{nodo.dado.cor}{nodo.dado.nro}")

        print("Lista de Espera:")
        print(" -> ".join(lista_espera))

    def __iter__(self):
        nodo = self.head
        while nodo is not None:
            yield nodo
            nodo = nodo.proximo

    def inserir(self):
        # fmt:off
        cor = input("""
    Digite:
    A - Amarelo (Prioridade)
    V - Vermelho

    Informe a cor do cartao: """).strip().upper()

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
            self.inserir_sem_prioridade(nodo)
        elif cor == "A":
            self.inserir_com_prioridade(nodo)

    def inserir_sem_prioridade(self, nodo: Elemento):
        if self.head is None:
            self.head = nodo
            return

        nodo_atual = self.head
        while nodo_atual.proximo is not None:
            nodo_atual = nodo_atual.proximo

        nodo_atual.proximo = nodo

    def inserir_com_prioridade(self, nodo):
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

    def atender_paciente(self):
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


def main():

    lista_hospitalar = ListaHospitalar()
    while True:
        print(
            """
 ________________________
| Atendimento Hospitalar |
 ------------------------
"""
        )
        print("1 - Adicionar paciente a fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")

        opcao = input("Digite sua opcao: ").strip()

        if opcao == "1":
            lista_hospitalar.inserir()
        elif opcao == "2":
            lista_hospitalar.imprimir_lista_espera()
        elif opcao == "3":
            lista_hospitalar.atender_paciente()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opcao invalida...Escolha novamente.")


if __name__ == "__main__":
    main()
