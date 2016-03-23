#!/usr/bin/python

import sys, getopt

file_in  = 'test.c'
file_out = 'saida.tokens'

# Parse dos nomes de arquivos de entrada e saida na linha de comado
def get_cmdline_args(argv):

   global file_in, file_out

   try:
      opts, args = getopt.getopt(argv,"hi:o:q:",["ifile=","ofile=","quiet="])
   except getopt.GetoptError:
      print 'Usage: ' + sys.argv[0] + ' [-q] -i <inputfile> -o <outputfile>'
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         print 'Usage: ' + sys.argv[0] + '[-q] -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         file_in  = arg
      elif opt in ("-o", "--ofile"):
         file_out = arg

   if opt not in ("-q", "--quiet"):
      print 'Input  file: ', file_in
      print 'Output file: ', file_out

	

def create_token(token):
   data_type     = ['int', 'char', 'float', 'string', 'const']
   special_chars = ['{', '}', '[', ']', '(', ')', ';']
   op_arit       = ['+', '-', '*', '/', '#']
   reserved      = ['for', 'while', 'do', 'if', 'else', 'main']

   print "token: %s" % (token)

   if (token in data_type):
      return "<type;%s>" % (token)

   if (token in special_chars):
      return "<%s;>" % (token)

   if (token in op_arit):
      return "<op_arit;%s>" % (token)

   if (token == '='):
      return "<=;>"

   if (token == 'main'):
      return "<main;%s>" % (token)

   return "<id;%s>" % (token)

def obterToken(fp, ftell):
   delim = ['{', '}', '(', ')', ';']

   init_token = False

   # reposiciona o fp no arquivo
   fp.seek(ftell)

   while True:
      ch = fp.read(1)
      if (ch = ' '):
         if (init_token):
            # retorno token
      

      if init_token:
         break
         



# main program
if __name__ == "__main__":
	
   if (len(sys.argv) > 1):
      get_cmdline_args(sys.argv[1:])
   
   source = open(file_in, 'r');
   is_digit           = False
   start_token        = True
   is_comment         = False
   can_be_comment     = False
   can_be_end_comment = False
   token = ""

   for line in source:
      for ch in ' '.join(line.split()):
         print source.tell()
         if (not is_comment):
            if (ch == '/'):
               can_be_comment = True

            if (can_be_comment and ch == '*'):
               can_be_comment = False
               is_comment = True

            # valid code
            if (not is_comment and not can_be_comment):
               if (ch == ' ' or ch == ';'):
                  start_token = True
                  create_token(token)
                  token = ""

               elif (ch.isdigit() and start_token):
                  token += ch

               elif (ch == '='):
                  create_token(ch)
                  token = ""

               else:
                  token += ch
                  #print ch

         # comment
         else:
            if (ch == '*'):
               can_be_end_comment = True

            if (ch == '/' and can_be_end_comment == True):
               is_comment = False

