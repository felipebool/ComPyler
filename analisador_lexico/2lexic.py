def has_special_char(line):
   special_chars = ['{', '}', '<', '>']

   if (not any(schar in line for schar in special_chars)):
      return False
   return True
      

def normalize_line(line):
   special_chars = ['{', '}', '<', '>']

   if has_special_char(line):
      for schar in special_chars:
         aux = line.replace(schar, ' ' + schar + ' ')
         line = aux
      return ' '.join(aux.split())

   return ' '.join(line.split())

if __name__ == "__main__":
   source = open('test.c', 'r')

   for line in source:
      if (line[0] != '\n'):
         print normalize_line(line)

