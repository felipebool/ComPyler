#!/usr/bin/env python
# -*- coding: utf-8 -*-

#"THE BEER-WARE LICENSE" (Revision 42):
#<raphael.ribas@gmail.com> wrote this file. As long as you retain this notice you
#can do whatever you want with this stuff. If we meet some day, and you think this
#stuff is worth it, you can buy me a beer in return. Raphel Henrique Ribas

import sys, os
from gramatica import Gramatica
from slr import Slr

def le_grammar(arquivo):
    f = file(arquivo)
    conta = 0
    regras = list()
    for linha in f:
        conta += 1
        linha = linha.rstrip(os.linesep)
        if linha == '' or linha[0] == '#':
            continue
        regra = tuple(linha.split())
        if len(regra) < 2 or regra [1] != '->':
            raise Exception('Erro: %s:%d' % (arquivo, conta))
        regras.append((regra[0],(regra[2:])))
    return regras

def main(argv):
    if len(argv) > 3 or len(argv) < 2:
        print 'Usage: %s <gramatica> [<tokens>]' % argv[0]
    producoes = le_grammar(argv[1])

    grammar = Gramatica(producoes, producoes[0][0])
    slr = Slr(grammar)
    if len(argv) == 3:
        tokens = file(argv[2]).read().split()

        slr.parse(tokens)

if __name__ == '__main__':
	main(sys.argv)
