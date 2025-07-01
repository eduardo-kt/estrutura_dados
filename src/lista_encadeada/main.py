"""
main.py

Lista Encadeada - fluxo principal do projeto

Descrição: Aplicativo que gerencia lista de pacientes em espera

Autor: Eduardo K Teixeira

"""

# TODO: (A) implementar uma lista encadeada simples
# TODO: (B) implementar função inserirSemPrioridade(nodo)
# TODO: (C) implementar função inserirComPrioridade(nodo)
# TODO: (D) implementar função inserir()
# TODO: (E) implementar função imprimirListaEspera()
# TODO: (F) implementar função atenderPaciente()

# TODO: (H) implementar teste do sistema


# (G) implementar menu de utilização do sistema
def menu():
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
            print("Funcao Inserir()\n")
            # função inserir()
        elif option == "2":
            print("Funcao ImprimirLista()\n")
            # função imprimirListaEspera()
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
