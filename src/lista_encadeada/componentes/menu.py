# src/lista_encadeada/componentes/menu.py

from lista_encadeada.componentes.lista import ListaHospitalar


def menu():
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

        opcao = escolher_opcao()

        if opcao == "1":
            lista_hospitalar.inserir()
        elif opcao == "2":
            lista_hospitalar.imprimirListaEspera()
        elif opcao == "3":
            lista_hospitalar.atenderPaciente()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opcao invalida...Escolha novamente\n")


def escolher_opcao():
    try:
        opcao = input("Digite sua opcao: ")
    except Exception:
        print("Digite uma opcao valida")
        opcao = "99"

    return opcao


if __name__ == "__main__":
    menu()
