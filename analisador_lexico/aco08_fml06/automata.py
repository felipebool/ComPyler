#!/usr/bin/python

import grammar as grammar
import error_messages as error

# TODO: remove this 
import sys

# TODO
# - line counting
# - should I remove the eof checking? Oo

def skip_blank(fp):
   """Skip blank spaces till next non blank character"""
   symbol = fp.read(1)

   while True:
      if not symbol.isspace():
         fp.seek(fp.tell() - 1)
         break
      symbol = fp.read(1)
# ------------------------------------------------------------------------------

def skip_comment(fp):
   """Skip comment and put put fp in the next character after end comment"""
   window = fp.read(1)

   while True:
      symbol = fp.read(1)

      if len(symbol) == 0:
         return {'error': error.MISSING_END_COMMENT} 

      window += symbol

      if window != '*/':
         window = window[1]
      else:
         break

   return {'comment':'comment'}
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
      if len(symbol) == 0:
         return {'error': error.IDENTIFIER_EOF}

      if symbol in grammar.forbidden:
         return {'error': error.FORBIDDEN_SYMBOL % (symbol)}

      if symbol in grammar.delimiters:
         fp_pos = fp.tell()
         break

      if symbol in grammar.op_arit or symbol == '=':
         fp_pos = fp.tell()
         break

      lexeme += symbol
      symbol = fp.read(1)

   if lexeme in grammar.data_type:
      token = {'token': "<type;%s>" % (lexeme)}
   elif lexeme in grammar.reserved: 
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
      if len(symbol) == 0:
         return {'error': error.IDENTIFIER_EOF}

      if symbol in grammar.forbidden:
         return {'error': error.FORBIDDEN_SYMBOL % (symbol)}

      if symbol in grammar.delimiters:
         fp_pos = fp.tell()
         fp.seek(fp_pos - 1)
         break

      lexeme += symbol

      if symbol.isalpha():
         return {'error': error.ID_OR_NUMBER}

      if symbol == '.':
         if has_point:
            return {'error': error.EXTRA_DOTS_NUMBER}
         else:
            has_point = True

         fp_pos = fp.tell()
         symbol = fp.read(1)

         if not symbol.isdigit():
            # FIXME: this error message is not being showed
            return {'error': error.DOT_WITHOUT_NUMBER}
         else:
            fp.seek(fp_pos)

      if symbol in grammar.delimiters:
         break

      symbol = fp.read(1)
   
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
      fp_pos = fp.tell()
      lexeme += fp.read(1)

      if lexeme == '/*':
         token = skip_comment(fp)

      if lexeme in grammar.op_arit:
         token = {'token': "<op_arit;%s>" % (lexeme)}

      
      if not lexeme[1] in grammar.op_arit:
         token = {'token': "<op_arit;%s>" % (symbol)}
         fp.seek(fp_pos)


   return token
# ------------------------------------------------------------------------------

def is_logical_op_or_attribution(fp, ch):
   symbol = ch
   lexeme = symbol
   token = {}

   if lexeme in grammar.op_logic:
      token = {'token': "<op_log;%s>" % (lexeme)}

   if lexeme == '=':
      token = {'token': "<attr;%s>" % (lexeme)}

   fp_pos = fp.tell()
   lexeme += fp.read(1)

   if symbol in grammar.forbidden:
      return {'error': error.FORBIDDEN_SYMBOL % (symbol)}

   if lexeme in grammar.op_logic:
      token = {'token': "<op_log;%s>" % (lexeme)}
   else:
      fp.seek(fp_pos)
   
   return token
# ------------------------------------------------------------------------------

def is_special_char(fp, ch):
   token = {'token': "<;%s>" % (ch)}
   return token
# ------------------------------------------------------------------------------

# TODO: deal with string/char without closing "|'
def is_string_char_value(fp, ch):
   symbol = ch
   lexeme = symbol

   # char
   if symbol == '\'':
      symbol = fp.read(1)
      lexeme += symbol

      symbol = fp.read(1)
      if not symbol == '\'':
         return {'error': error.BIG_CHAR}
      else:
         lexeme += symbol

      token = {'token': "<%s;char_value>" % (lexeme)}

   # string
   else:
      symbol = fp.read(1)
      if symbol == "\"":
         return {'error': error.EMPTY_STRING}

      while True:
         symbol = fp.read(1)
         lexeme += symbol
         if symbol == "\"":
            token = {'token': "<%s;str_value>" % (lexeme)}
            break

   return token
# ------------------------------------------------------------------------------

def get_token(fp):
   skip_blank(fp)
   symbol = fp.read(1)
   token = {}

   if symbol in ['"', '\'']:
      token = is_string_char_value(fp, symbol)

   # not part 
   if symbol in grammar.forbidden:
      token = {'error': error.FORBIDDEN_SYMBOL % (symbol)}

   if symbol.isalpha():      
      token = is_alpha(fp, symbol)

   elif symbol.isdigit():
      token = is_digit(fp, symbol)

   elif symbol in grammar.op_arit:
      token = is_arithmetic_op(fp, symbol)

   elif symbol in grammar.op_logic or symbol == '=':
      token = is_logical_op_or_attribution(fp, symbol)

   elif symbol in grammar.spec_chars:
      token = is_special_char(fp,symbol)

   elif symbol == '\n':
      token = {'eof': 'eof'}

   skip_blank(fp)
   return token

