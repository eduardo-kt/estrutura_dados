# src/tabela_hash/componentes/menu_principal.py

from tabela_hash.componentes.funcoes_aux import inserir_estado, remover_estado
from tabela_hash.componentes.config import INICIAL


def menu():

    while True:
        print(
            """
     _______________________
    | EMPLACAMENTO VEICULAR |
     -----------------------
"""
        )
        print("1 - Inserir na tabela hash")
        print("2 - Remover na tabela hash")
        print("3 - Listar a tabela hash")
        print("4 - Sair")

        opcao = input("Escolha uma opcao: ")
        opcao = opcao.strip()

        if opcao == "1":
            print("FUNÇÃO INSERIR NA TABELA HASH...")
            inserir_estado(INICIAL.tabelahash, INICIAL.n)
        elif opcao == "2":
            print("FUNÇÃO REMOVER NA TABELA HASH")
            remover_estado(INICIAL.tabelahash, INICIAL.n)
        elif opcao == "3":
            print("FUNÇÃO LISTAR A TABELA HASH")
            print(INICIAL.tabelahash)
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opcao invalida. Retornando ao menu principal...")


if __name__ == "__main__":
    menu()
