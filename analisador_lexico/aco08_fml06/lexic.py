#!/usr/bin/python

import sys, getopt
import automata

if __name__ == "__main__":
   source = sys.argv[1]
   dest = open('output.tokens', 'w')
    
   with open(source) as fp:
      while True:
         token = automata.get_token(fp)
         if not token.has_key('comment'):

            if token.has_key('error'):
               print token.get('error')
               sys.exit()

            if token.has_key('token'):
               dest.write(token.get('token') + '\n')

            if token.has_key('eof'):
               print "\n%d lines were scanned, everything is fine!\n" % (token.get('eof'))
               sys.exit()
