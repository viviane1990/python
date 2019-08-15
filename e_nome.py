def formata_nome(nome_full):
    nome_formatado = [nome.capitalize() for nome in nome_full.split()]
    formato = ' '.join(nome_formatado)
    formato = formato.replace(' Da' ,' da ').replace(' De ' ,' de ').replace(' Dos ' ,' dos ')
    return formato

