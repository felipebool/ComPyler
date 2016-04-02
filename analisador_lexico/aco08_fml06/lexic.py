#!/usr/bin/python

import sys, getopt
import automata

if __name__ == "__main__":
   source = sys.argv[1]
    
   with open(source) as fp:
      while True:
         token = automata.get_token(fp)
         if not token.has_key('comment'):

            if token.has_key('error'):
               print token.get('error')
               sys.exit()

            if token.has_key('token'):
               print token.get('token')

            if token.has_key('eof'):
               sys.exit()
         else:
            print token.get('comment')
