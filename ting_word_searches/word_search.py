from ting_file_management.queue import Queue


def word_and_search(word: str, row: str, index: int, search_exits: str):
    lista_de_linhas = []
    if word.lower() in row.lower() and search_exits == 'exists':
        lista_de_linhas.append({"linha": index+1})
    elif word.lower() in row.lower() and search_exits == 'search':
        lista_de_linhas.append({"linha": index+1, "conteudo": row})
    return lista_de_linhas


def project_objects(word: str, name_file: str, rows: list, lista: list):
    lista.append({
                "palavra": word,
                "arquivo": name_file,
                "ocorrencias": rows
            })


def rows_word(word: str, instance: Queue, search_exits: str):
    lista_de_objetos = []
    rows = []
    for i in instance.data:
        for index, row in enumerate(i['linhas_do_arquivo']):
            rows += word_and_search(word, row, index, search_exits)
        if len(rows) != 0:
            project_objects(word, i['nome_do_arquivo'], rows, lista_de_objetos)
    return lista_de_objetos


def exists_word(word: str, instance: Queue):
    return rows_word(word, instance, 'exists')


def search_by_word(word: str, instance: Queue):
    return rows_word(word, instance, 'search')
