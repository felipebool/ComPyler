#!/usr/bin/python

import grammar as gram

# TODO: remove this 
import sys

def skip_blank(fp):
   """
      skip_blank puts fp in the next non blank character
   """
   while True:
      symbol = fp.read(1)
      if not symbol.isspace():
         fp.seek(fp.tell() - 1)
         break
# ------------------------------------------------------------------------------

def skip_comment(fp):
   """
      skip_comment put fp in the next non blank character after
      the end comment, if end comment is missing, skip_comment
      return -1
   """
   window = fp.read(1)

   while True:
      symbol = fp.read(1)

      if symbol == '':
         return {'error': 'Lexical error: you should check your comments'}

      window += symbol

      if window != '*/':
         window = window[1]
      else:
         break
# ------------------------------------------------------------------------------


def is_alpha(fp, ch):
   """
      Return an alpha token. Alpha tokens can be identifiers,
      reserved words and language types (int, float, string
      and char), is_alpha returns the file pointer (fp) in
      the next not blank character.
   """
   symbol = ch
   lexeme = ''

   while True:
      # end of file error
      if symbol == '':
         return {'error': 'Lexical error: EOF reached, maybe you forgot something...'}

      if symbol in gram.forbidden:
         return {'error': "Lexical error: \'%c\' is not part of the alphabet, champz!" % (symbol)}

      if symbol in gram.delimiters:
         fp_pos = fp.tell()
         break

      if symbol in gram.op_arit or symbol in gram. or symbol == '=':
         fp_pos = fp.tell()
         break

      lexeme += symbol
      symbol = fp.read(1)

   skip_blank(fp)

   if lexeme in gram.data_type:
      token = {'token': "<type;%s>" % (lexeme)}
   elif lexeme in gram.reserved: 
      token = {'token': "<reserved;%s>" % (lexeme)}
   else:
      token = {'token': "<id;%s>" % (lexeme)}

   fp.seek(fp_pos - 1)
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
   lexeme = ""
   token = {}

   while True:
      # end of file (is this an error?)
      if symbol == '':
         token = {'eof': True}
         break

      if symbol in gram.forbidden:
         return {'error': "Lexical error: \'%c\' is not part of the alphabet, champz!" % (symbol)}

      if symbol in gram.delimiters:
         fp_pos = fp.tell()
         fp.seek(fp_pos - 1)
         break

      lexeme += symbol

      if symbol.isalpha():
         return {'error': "Lexical error: there is a character inside your number, pal!"}

      if symbol == '.':
         if has_point:
            return {'error': "Lexical error: maybe you have a few extra dots inside a number, bro!"}
         has_point = True

         fp_pos = fp.tell()
         symbol = fp.read(1)

         if not symbol.isdigit():
            return {'error': "Lexical error: your number has a point not followed by more numbers, mate!"}
         else:
            fp.seek(fp_pos)

      if symbol in gram.delimiters:
         break

      symbol = fp.read(1)
   
   skip_blank(fp)
   token = {'token': "<num;%s>" % (lexeme)}
   return token
# ------------------------------------------------------------------------------


def is_arithmetic_op(fp, ch):
   """
      Return an arithmetic token or skip comment
   """
   symbol = ch
   lexeme = symbol

   if symbol in ['*', '#']:
      token = {'token': "<op_arit;%s>" % lexeme}

   if symbol in ['/', '+', '-']:
      lexeme += fp.read(1)

      if lexeme == '/*':
         skip_comment(fp)
         token = {'comment': True}

      if lexeme in gram.op_arit:
         token = {'token': "<op_arit;%s>" % (lexeme)}

   skip_blank(fp)
   return token
# ------------------------------------------------------------------------------

def is_logical_op_or_attribution(fp, ch):
   symbol = ch
   lexeme = symbol
   token = {}

   if lexeme in gram.op_logic:
      token = {'token': "<op_log;%s>" % (lexeme)}

   if lexeme == '=':
      token = {'token': "<attr;%s>" % (lexeme)}

   lexeme += fp.read(1)

   if symbol in gram.forbidden:
      return {'error': "Lexical error: \'%c\' is not part of the alphabet, champz!" % (symbol)}

   if lexeme in gram.op_logic:
      token = {'token': "<op_log;%s>" % (lexeme)}

   skip_blank(fp)
   return token
# ------------------------------------------------------------------------------

def is_special_char(ch):
   return {'token': "<;%s>" % (ch)}
# ------------------------------------------------------------------------------

def get_token(fp):
   skip_blank(fp)
   symbol = fp.read(1)
   token = {}

   # not part 
   if symbol in gram.forbidden:
      print "Lexical error: \'%c\' is not allowed"
      sys.exit()

   if symbol.isalpha():      
      token = is_alpha(fp, symbol)

   elif symbol.isdigit():
      token = is_digit(fp, symbol)

   elif symbol in gram.op_arit:
      token = is_arithmetic_op(fp, symbol)

   elif symbol in gram.op_logic or symbol == '=':
      token = is_logical_op_or_attribution(fp, symbol)

   elif symbol in gram.spec_chars:
      token = is_special_char(symbol)

   return token

