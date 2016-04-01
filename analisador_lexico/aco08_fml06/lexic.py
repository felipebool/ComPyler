#!/usr/bin/python

import sys, getopt
import automata

if __name__ == "__main__":
   source = sys.argv[1]
    
   with open(source) as fp:
      while True:
         token = automata.get_token(fp)
         if 'error' in token:
            print token['error']
            sys.exit

         if token == 'EOF':
            break
         print token

