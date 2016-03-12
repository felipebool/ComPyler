#!/usr/bin/python

def create_token(token):
   data_type     = ['int', 'char', 'float', 'string', 'const']
   special_chars = ['{', '}', '[', ']', '(', ')']
   op_arit       = ['+', '-', '*', '/', '#']

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

# main program
if __name__ == "__main__":
   source = open('test.c', 'r');

   for line in source:
      token = ""

      is_digit           = False
      start_token        = True
      is_comment         = False
      can_be_comment     = False
      can_be_end_comment = False

      for ch in ' '.join(line.split()):
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
                  print ch

         # comment
         else:
            if (ch == '*'):
               can_be_end_comment = True

            if (ch == '/' and can_be_end_comment == True):
               is_comment = False

