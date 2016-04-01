#!/usr/bin/python

import grammar as gram

# TODO: this function must keep track of the lines skipped
def skip_blank(fp):
   """
      skip_blank puts fp in the next non blank character
   """
   ign_list = [' ', '\t', '\n']

   while True:
      ch = fp.read(1)
      # TODO: use ch.isspace()
      if ch not in ign_list:
         fp.seek(fp.tell() - 1)
         break
# ------------------------------------------------------------------------------

# TODO: this function must keep track of the lines skipped
def skip_comment(fp):
   """
      skip_comment put fp in the next non blank character after
      the end comment, if end comment is missing, skip_comment
      return -1
   """
   can_be_end_comment = False
   is_comment = True

   while True:
      symbol = fp.read(1)

      # end of file error
      if symbol == '':
         return {'comment': False}

      if symbol == '*':
         can_be_end_comment = True
      else:
         can_be_end_comment = False

      if symbol == '/' and can_be_end_comment:
         is_comment = False

      if not is_comment:
         skip_blank(fp)
         return
# ------------------------------------------------------------------------------

def is_alpha(fp, ch):
   """
      Return an alpha token. Alpha tokens can be identifiers,
      reserved words and language types (int, float, string
      and char), is_alpha returns the file pointer (fp) in
      the next not blank character.
   """
   symbol = ch
   lexeme = symbol

   while True:
      # end of file error
      if symbol == '':
         break

      if symbol in gram.forbidden:
         error = "Lexical error: \'%c\' is not part of \
                  the alphabet, champz!" % (symbol)
         return {'error': error}

      if symbol in gram.delimiters:
         break

      lexeme += symbol
      symbol = fp.read(1)

   skip_blank(fp)
   if lexeme in gram.data_type:
      token = "<type;%s>" % (lexeme)
   elif lexeme in gram.reserved: 
      token = "<reserved;%s>" % (lexeme)
   else:
      token = "<id;%s>" % (lexeme)

   return token
# ------------------------------------------------------------------------------

def is_digit(fp, ch):
   """
      Return a number token. Number tokens are numbers, float or integer.
      The only characters allowed here are numbers (digits) and points (only
      one inside a lexeme
   """
   has_point = False
   symbol = ch
   lexeme = symbol

   while True:
      # end of file
      if symbol == '':
         break

      if symbol in gram.forbidden:
         error = "Lexical error: \'%c\' is not part of \
                  the alphabet, champz!" % (symbol)
         return {'error': error}

      if symbol.isdigit():
         lexeme += symbol

      else:
         if symbol == '.':
            fp_pos = fp.tell()

            if has_point:
               error = "Lexical error: maybe you have a few \
                        extra dots inside a number, bro!"
               return {'error': error}

            lexeme += symbol

            # check if character after point is another number
            symbol = fp.read(1)
            if not symbol.isdigit():
               error = "Lexical error: your number has a point \
               not followed by more numbers, mate!"
               return {'error': error}
            else:
               fp.seek(fp_pos)

            has_point = True

         if symbol in gram.delimiters:
            break

         if symbol.isalpha():
            error = "Lexical error: there is a character inside \
                     your number, pal!"
            return error

         lexeme += symbol
         symbol = fp.read(1)
   
   skip_blank(fp)

   token = "<num;%s>" % (lexeme)
   return token
# ------------------------------------------------------------------------------


def is_arithmetic_op(fp, ch):
   """
      Return an arithmetic token or skip comment
   """
   symbol = ch
   lexeme = symbol

   if symbol in ['*', '#']:
      token = "<op_arit;%s>" % lexeme

   if symbol in ['/', '+', '-']:
      lexeme += fp.read(1)

      if lexeme == '/*':
         return skip_comment(fp)

      if lexeme in gram.op_arit:
         token = "<op_arit;%s>" % (lexeme)

   skip_blank(fp)
   return token
# ------------------------------------------------------------------------------

def is_logical_op_or_attribution(fp, ch):
   symbol = ch
   lexeme = symbol

   if lexeme in gram.op_logic:
      token = "<op_log;%s>" % (lexeme)

   if lexeme == '=':
      token = "<attr;%s>" % (lexeme)

   lexeme += fp.read(1)

   if symbol in gram.forbidden:
      error = "Lexical error: \'%c\' is not part of \
               the alphabet, champz!" % (symbol)
      return {'error': error}   

   if lexeme in gram.op_logic:
      token = "<op_log;%s>" % (lexeme)

   # TODO: here we can have errors like: <#

   skip_blank(fp)
   return token
# ------------------------------------------------------------------------------

def is_special_char(ch):
   symbol = ch
   lexeme = symbol
   token = "<;%s>" % (lexeme)
   return token
# ------------------------------------------------------------------------------

def get_token(fp):
   skip_blank(fp)
   symbol = fp.read(1)

   # not part 
   if symbol in gram.forbidden:
      print "Lexical error: \'%c\' is not allowed"
      sys.exit()

   if symbol.isalpha():      
      token = is_alpha(fp, symbol)

   elif symbol.isdigit():
      token = is_digit(fp, symbol)

   elif symbol in gram.op_arit:
      token = is_arithmetical_op(fp, symbol)

   elif symbol in gram.op_logic or symbol == '=':
      token = is_logical_op_or_attribution(fp, symbol)

   elif symbol in gram.spec_chars:
      token = is_special_char(symbol)

   return token

