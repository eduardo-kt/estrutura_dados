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

        option = choose_option()

        if option == "1":
            lista_hospitalar.inserir()
        elif option == "2":
            lista_hospitalar.imprimirListaEspera()
        elif option == "3":
            print("Funcao atenderPaciente()\n")
            # função atenderPaciente()
        elif option == "4":
            print("Saindo do programa...")
            break
        else:
            print("Invalid Option...")


def choose_option():
    try:
        option = input("Digite sua option: ")
    except Exception:
        print("Digite uma option valid")
        option = "99"

    return option


if __name__ == "__main__":
    menu()
