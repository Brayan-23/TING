def exists_word(word, instance):
    lista_de_objetos = []
    lista_de_linhas = []
    for i in instance.data:
        for index, row in enumerate(i['linhas_do_arquivo']):
            if word.lower() in row.lower():
                lista_de_linhas.append({"linha": index+1})
                continue
        if len(lista_de_linhas) != 0:
            lista_de_objetos.append({
                "palavra": word,
                "arquivo": i['nome_do_arquivo'],
                "ocorrencias": lista_de_linhas
            })
        print(lista_de_objetos)
    return lista_de_objetos


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
