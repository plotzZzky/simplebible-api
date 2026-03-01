#!/usr/bin/env python3

from api.db import find_in_bible
from api.utils import format_query
import sys


def simple_bible(book=None, capt=None, vers=None):
    # função para exibir o trecho da biblia no terminal
    query = find_in_bible(book, capt, vers)
    result = format_query(query, 'txt')
    print(result)


if __name__ == '__main__':
    # recebe o livro e formata o nome
    arg_1 = sys.argv[1] if len(sys.argv) > 1 else None
    if arg_1:
        arg_book = arg_1.replace('_', ' ').title()
    else:
        arg_book = arg_1

    # recebe o segundo argumento, e formata corretamente
    arg_2 = sys.argv[2] if len(sys.argv) > 2 else None

    # formata o capitulo do livro
    arg_capt = arg_2.split(':')[0] if arg_2 else None

    # formata o versiculo se tiver um segundo argumento
    arg_vers = arg_2.split(':')[1] if arg_2 and ':' in arg_2 else None

    simple_bible(arg_book, arg_capt, arg_vers)  # chama a função
