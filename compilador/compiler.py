#!/usr/bin/python

import sys, os, getopt

sys.path.insert(0, '../analisador_lexico/aco08_fml06/')
import automata

sys.path.insert(0, '../analisador_sintatico/')
from gramatica import Gramatica
from slr import Slr

def import_gram(gfile):
    f = file(gfile)
    conta = 0   
    prods = list()

    for linha in f:
        conta += 1
        linha = linha.rstrip(os.linesep)

        if linha == '' or linha[0] == '#':
            continue

        regra = tuple(linha.split())

        if len(regra) < 2 or regra[1] != '->':
            raise Exception('Erro: %s:%d' % (arquivo, conta))

        prods.append((regra[0],(regra[2:])))
    return prods


def main(argv):
    # importa gramatica from 
    producoes = import_gram('minic.gram')

    source = sys.argv[1]
    dest = open('output.tokens', 'w')

    symbol_table = list()
    
    with open(source) as fp: 
        while True:
            token = automata.get_token(fp)
            if not token.has_key('comment'):
                # AQUI -------------------------------------------------------------------
                # ------------------------------------------------------------------------




                if token.has_key('error'):
                    print token.get('error')
                    sys.exit()

                if token.has_key('token'):
                    dest.write(token.get('token') + '\n')


                    if (token.get('token').split(';')[0])[1:] == "id":
                        identifier = (token.get('token').split(';')[1])[:-1]
                        table_entry = {'identifier': identifier} 
                        symbol_table.append(table_entry)

                if token.has_key('eof'):
                    print "\n%d lines were scanned, everything is fine!\n" % (token.get('eof'))

#                    print "SYMBOL TABLE"
#                    for entry in symbol_table:
#                        print "identifier\t%s" % (entry.get('identifier')) 

                    sys.exit()

    



if __name__ == '__main__':
    main(sys.argv)
