#!/usr/bin/python

# main program
if __name__ == "__main__":
   source = open('test.c', 'r');

   lines = 0
   chars = 0

   for line in source:
      lines += 1
      token = ""

      is_comment         = False
      can_be_comment     = False
      can_be_end_comment = False

      for ch in ' '.join(line.split()):
         chars += 1
         if (not is_comment):
            if (ch == '/'):
               can_be_comment = True

            if (can_be_comment and ch == '*'):
               can_be_comment = False
               is_comment = True

            if (not is_comment and not can_be_comment):
               if (ch != ' ' and ch != ';'):
                  token = token + ch
               else:
                  print token
                  token = ""

         else:
            if (ch == '*'):
               can_be_end_comment = True

            if (ch == '/' and can_be_end_comment == True):
               is_comment = False

