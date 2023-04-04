import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


#
