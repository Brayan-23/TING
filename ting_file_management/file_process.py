import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file: str, instance: Queue):
    linhas = txt_importer(path_file)
    obj = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(linhas),
        "linhas_do_arquivo": linhas
    }
    if len(instance) == 0:
        instance.enqueue(obj)
        print(obj, file=sys.stdout)
    if len(instance) != 0:
        for i in range(len(instance)-1):
            result = instance.search[i]
            if result['nome_do_arquivo'] == path_file:
                return None
    else:
        instance.enqueue(obj)
        print(obj, file=sys.stdout)


def remove(instance: Queue):
    if len(instance) == 0:
        print('Não há elementos', file=sys.stdout)
    else:
        removed = instance.dequeue()
        name = removed['nome_do_arquivo']
        print(f'Arquivo {name} removido com sucesso')


def file_metadata(instance: Queue, position: int):
    try:
        print(instance.search(position), file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
