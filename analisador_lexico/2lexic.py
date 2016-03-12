#
# esta versão lê o arquivo de uma maneira diferente.
# não gostei de verdade de nenhuma das soluções até
# agora
#


def has_special_char(line):
   special_chars = ['{', '}', ';']

   if (not any(schar in line for schar in special_chars)):
      return False
   return True
      

def normalize_line(line):
   special_charyys = ['{', '}', '<=', '>=']

   if has_special_char(line):
      for schar in special_chars:
         aux = line.replace(schar, ' ' + schar + ' ')
         line = aux
      return ' '.join(aux.split())

   return ' '.join(line.split())

def create_token(token):
   types = ['int', 'float', 'char', 'string']
   special_chars = ['{', '}', '>=', '<=']
   open_comment = '/*'
   new_str = ""

   for t in types:
      if (t == token):
         return "<type;%s>" % (token)

   for sp in special_chars:
      if (sp == token):
         return "<%s;>" % (token)

   for 

   return token

if __name__ == "__main__":
   special_chars = ['{', '}', ';']
   source = open('test.c', 'r')

   for line in source:
      if (line[0] != '\n'):
         tokens = normalize_line(line).split(' ')
         for tk in tokens:
            print create_token(tk)

