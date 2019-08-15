def calcula_tamanho(texto):
    tamanho = (len(texto))

    if tamanho > 15:
        return texto[:12] + '...'
    else:
        return texto

