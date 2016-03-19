#!/usr/bin/python

# Language definition ----------------------------------------------------------
special_chars = ['{', '}', '(', ')', ';']
types         = ['int', 'float', 'char', 'string']
reserved      = ['for', 'while', 'do', 'if', 'else', 'main']
op_arit       = ['+', '-', '*', '/', '#']

OPEN_COMMENT  = '/*'
CLOSE_COMMENT = '*/'

BLANKSPACE    = ' '
# ------------------------------------------------------------------------------


def create_token(tk):
   global special_chars
   global types
   global reserved
   global op_arit

   if tk in special_chars:
      return "<;%s>" % (tk)
   elif tk in types:
       return "<type;%s>" % (tk)
   elif tk in reserved:
       return "<reserved;%s>" % (tk)
   elif tk in op_arit:
       return "<op_arit;%s>" % (tk)
   else:
       return "<unknow;%s>" % (tk)


# main program
if __name__ == "__main__":
   WHITESPACE    = [' ','\n', '\t']
   source = open('test.c', 'r')
   token = ""

   is_comment         = False
   can_be_comment     = False
   can_be_end_comment = False

   for line in source:
      
      for ch in line:
         if ch == '/':
            can_be_comment = True

         if ch == '*' and can_be_comment:
            is_comment = True
            can_be_comment = False

         if ch == '*':
            can_be_end_comment = True

         if ch == '/' and can_be_end_comment:
            is_comment = False
            can_be_end_comment = False

         if not ch in WHITESPACE and not is_comment:
            if ch == ';':   
               token += ch

         else:
            if len(token) > 0:
               print "\"%s\" - %d" %(token, len(token))
            token = ""













