#!/usr/bin/python

import re

# TODO list
# - ignorar comentarios
# - casos que nao funciona
#  -- a+c
#  -- a++
#  -- +c
#  -- a==
# - fazer as opcoes -i e -o: alexandre
# - fazer teste para string (create_token): bol
# - fazer test para char (create_token): bol
# - implementar contagem de linhas
# - implementar contagem de caracteres

# debug, ajuda a evidenciar os casos que a gente nao cobre.
# podemos usa-la mais pra frente pra retornar erro lexico...

   

# testa tipo do token e o retorna formatado
def create_token(tk):

   types  = ['int', 'float', 'char', 'string', 'const']
   reserv = ['for', 'if', 'else', 'while']
   delim  = ['{', '}', '(', ')', ';']

   op_arit  = ['+', '-', '*', '=']
   op_rel   = ['>', '<', '>=', '<=',]
   op_log   = ['==', '!=']

   id_pattern   = re.compile('[a-zA-Z]+[a-zA-Z0-9]*')
   str_pattern  = re.compile('\"[a-zA-Z]*\"')
   char_pattern = re.compile('\'[a-z0-9]\'')

   if tk in types:
      return "<type;%s>" % (tk)

   if tk in op_arit:
      return "<op_arit;%s>" % (tk)

   if tk in op_rel:
      return "<op_rel;%s>" % (tk)

   if tk in op_log:
      return "<op_log;%s>" % (tk)

   if tk in delim:
      return "<%s;>" % (tk)

   if tk in reserv:
      return "<%s;>" % (tk)

   if tk.isdigit():
      return "<num;%s>" % (tk)

   if id_pattern.match(tk):
      return "<id;%s>" % (tk)

   if str_pattern.match(tk):
      return "<str;%s>" % (tk)

   if char_pattern.match(tk):
      return "<char;%s>" % (tk)


   return "<UNKNOW;%s>" % (tk)



def obter_token(fp, fpos):
   delim = ['{', '}', '(', ')', ';']
   token = ""

   is_token = False
   fp.seek(fpos)

   while True:
      # aqui vai a logica que ignora comentarios
      ch = fp.read(1)

      if not ch == '\n':
         if ch in delim:
            if len(token) == 0:
               return [create_token(ch), fp.tell()]
            else:
               return [create_token(token), fp.tell() - 1]

         if not ch == ' ':
            is_token = True

         if ch == ' ' and is_token:
            return [create_token(token), fp.tell()]

         if is_token:
            token += ch


if __name__ == "__main__":
   source = open('test.c', 'r')

   fetch = obter_token(source, 0)
   while True:
      #print "\"" + fetch[0] + "\"" + ':' +  str(fetch[1])
      print fetch[0]
      fetch = obter_token(source, fetch[1])

