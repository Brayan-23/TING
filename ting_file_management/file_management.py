import sys


def txt_importer(path_file: str):
    if not path_file.endswith('.txt'):
        print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file, encoding='utf-8', mode='r') as file:
            leitura = file.read().split('\n')
            return leitura
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
