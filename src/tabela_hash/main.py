"""
src/tabela_hash/main.py

Tabela Hash - fluxo principal do projeto

Descrição: Aplicativo para emplacamento de veiculos

Autor: Eduardo K Teixeira
github: https://github.com/eduardo-kt/estrutura_dados.git
"""

from tabela_hash.componentes.menu_principal import menu

# TODO: tabela hash com endereçamento em cadeia de
#       10 posições representando os números de 0-9
#       que irão representar os 26 estados + DF
# TODO: cada posição do vetor deve ser uma lista encadeada
# TODO: a entrada da função hash é uma string 2 letras representando a UF
# TODO: UF==DF deve retornar sempre 7
# TODO: UF!=DF regra posição = (ascii(char1) + ascii(char2))MOD10
# TODO: implementar tabela hash de 10 posições (valor inicial None)
# TODO: implementar lista encadeada simples com
#       Nodo(UF,nomeEstado, ponteiro para próximo). As 10 posições da tabela
#       hash representam a cabeça de cada lista(head).
# TODO: implementar inserção no início da lista encadeada
#       (cada novo elemento sempre ser inserido no início da lista)
# TODO: implementar a impressão da tabela hash (imprimir UF que
#       estão na tabela, separados por posição)
# TODO: implementar a função hash conforme enunciado
# TODO: implementar a inserção das UF utilizando a função hash (ñ precisa
#       usuário digitar, pode ser hard coded)
# TODO: inserir além das UF, uma UF fictícia [UF,nome] = [ET, Eduardo Teixeira]
# TODO: imprimir tabela hash antes de inserir qualquer informação
# TODO: imprimir tabela hash após inserir as UF
# TODO: imprimir tabela hash após inserir UF fictícia

menu()
