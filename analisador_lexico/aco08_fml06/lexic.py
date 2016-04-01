#!/usr/bin/python

# ------------------------------------------------------------------------------
# TODO: CRIAR A TABELA DE SIMBOLOS
# ------------------------------------------------------------------------------

import sys, getopt

file_in  = 'test.c'
file_out = 'saida.tokens'

# ------------------------------------------------------------------------------
def skip_blank(fp):
   ign_list = [' ', '\t', '\n']
   error = []

   while True:
      ch = fp.read(1)
      if ch not in ign_list:
         fp.seek(fp.tell() - 1)
         break
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
def get_token(fp):
   data_type  = ['int', 'char', 'float', 'const', 'string']
   spec_chars = ['{', '}', '[', ']', '(', ')', ';', '"', '\'']
   op_arit    = ['+', '++', '-', '--', '*', '/', '#']
   op_logic   = ['>', '<', '>=', '<=', '==', '!', '!=']
   reserved   = ['for', 'while', 'do', 'if', 'else', 'main']
   separators = [';', ',']
   ign_list   = [' ', '\t', '\n']

   delimiters = [' ', '\t', '\n', '(', ')', '{', '}', ';']

   skip_blank(fp)
   ch = fp.read(1)
   tk = ""

   # Operadores aritmeticos ----------------------------------------------------
   if ch in op_arit:
      tk = ch
      if tk in ['/', '+', '-']:
         tk += fp.read(1)
         # Trata se eh comentario de bloco - ERROR DE COMENTARIO TRATA AQUI
         if tk == '/*':
            while tk != '*/':
               ch = fp.read(1)
               if not ch:
                  return "EOF"
               tk = tk[1:] + ch
            return get_token(fp)
         # Trata operadores com dois caracteres: ++ e --
         if tk in op_arit:
            return "<op_arit;%s>" % (tk)
         else:
            fp.seek(fp.tell() - 1)
      # Operadores de um soh caractere
      return "<op_arit;%s>" % (ch)
   # ---------------------------------------------------------------------------
		
   ### Operadores logicos e atribuicao
   if ch in op_logic or ch == '=':
      tk = ch + fp.read(1)
      if tk in op_logic:
         return "<op_log;%s>" % (tk)
      else:
         fp.seek(fp.tell() - 1)
         if ch == '=':
            return "<attrib;%s>" % (ch)
         else:
            return "<op_log;%s>" % (ch)

   ### Caracteres especiais ###
   if ch in spec_chars:
      tk = ch
      return "<%s;>" % (tk)

   ### Numeros (inteiros e ponto flutuante) ### ERRO
   if ch.isdigit():
      tk  = ch
      while ch.isdigit() or ch == '.':
         ch = fp.read(1)
         tk += ch
      tk = tk[:-1]
      fp.seek(fp.tell() - 1)
      return "<num;%s>" % (tk)


   ### Tipos de dados, Palavras reservadas, Identificadores
   if ch.isalpha():
      tk = ch
      while not ch == ' ':
         tk += ch
         ch = fp.read(1)

      tk = tk[:-1]
      fp.seek(fp.tell() - 1)

      if tk in data_type:
         return "<type;%s>" % (tk)
      elif tk in reserved: 
         return "<reserved;%s>" % (tk)
      else:
         return "<id;%s>" % (tk)

   ### Nenhuma das opcoes acima
   return ch

# main -------------------------------------------------------------------------
if __name__ == "__main__":
   source = sys.argv[1]
    
   with open(source) as fp:
      while True:
         token = get_token(fp)
         if token == 'EOF':
            break
         print token


#      while (ch) and (ch not in separators) and (ch not in spec_chars) and (ch not in ign_list):
#      while ch not in separators and ch not in spec_chars and ch not in ign_list:
#      while ch not in delimiters:
