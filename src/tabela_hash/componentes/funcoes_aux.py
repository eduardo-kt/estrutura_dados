def hashFunc(k, n):
    return k % n


def hashFuncSigla(k, n):
    k = list(k)
    return (ord(k[0]) + ord(k[1])) % n


def inserir_estado(tabela_hash, n):
    chave = input("Digite a sigla de um estado: ")
    chave = chave.strip()
    pos = hashFuncSigla(chave, n)
    if tabela_hash[pos] is None:
        tabela_hash[pos] = chave
    else:
        print("Já existe um dado neste lugar!")


def remover_estado(tabela_hash, n):
    chave = int(input("Digite o que deseja remover: "))
    pos = hashFuncSigla(chave, n)
    if tabela_hash[pos] == chave:
        tabela_hash[pos] = None
    else:
        print("Valor não localizado para a remoção!")
