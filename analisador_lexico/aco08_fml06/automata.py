#!/usr/bin/python

import grammar as grammar
import error_messages as error

def skip_blank(fp):
   symbol = fp.read(grammar.CHAR)

   while True:
      if not symbol.isspace():
         fp.seek(fp.tell() - 1)
         break
      symbol = fp.read(grammar.CHAR)
# ------------------------------------------------------------------------------


def skip_comment(fp):
   window = fp.read(grammar.CHAR)

   while True:
      symbol = fp.read(grammar.CHAR)

      if len(symbol) == 0:
         return {'error': error.MISSING_END_COMMENT} 

      window += symbol

      if window == grammar.OPENCOMMENT:
         return {'error': error.MISSING_END_COMMENT}

      if window != grammar.CLOSECOMMENT:
         window = window[1]
      else:
         break

   return {'comment':'comment'}
# ------------------------------------------------------------------------------


def is_alpha(fp, ch):
   """Return an alpha token (identifiers, reserved words and language types)"""
   symbol = ch
   lexeme = ''

   while True:
      if symbol in grammar.FORBIDDEN:
         return {'error': error.FORBIDDEN_SYMBOL % (symbol)}

      if symbol in grammar.DELIMITER:
         fp_pos = fp.tell()
         break

      if symbol in grammar.ARIT_OP or symbol == '=':
         fp_pos = fp.tell()
         break

      lexeme += symbol
      symbol = fp.read(grammar.CHAR)

   if lexeme in grammar.DATA_TYPE:
      token = {'token': "<type;%s>" % (lexeme)}
   elif lexeme in grammar.RESERVED: 
      token = {'token': "<reserved;%s>" % (lexeme)}
   else:
      token = {'token': "<id;%s>" % (lexeme)}

   fp.seek(fp_pos - 1)
   return token
# ------------------------------------------------------------------------------


def is_digit(fp, ch):
   """Return a number token"""
   has_point = False
   symbol = ch
   lexeme = ""
   token = {}

   while True:
      if symbol in grammar.FORBIDDEN:
         return {'error': error.FORBIDDEN_SYMBOL % (symbol)}

      if symbol in grammar.DELIMITER:
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

      if symbol in grammar.DELIMITER:
         break

      symbol = fp.read(grammar.CHAR)
   
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
      lexeme += fp.read(grammar.CHAR)

      if lexeme == grammar.OPENCOMMENT:
         token = skip_comment(fp)

      if lexeme in grammar.ARIT_OP:
         token = {'token': "<op_arit;%s>" % (lexeme)}

      
      if not lexeme[1] in grammar.ARIT_OP:
         token = {'token': "<op_arit;%s>" % (symbol)}
         fp.seek(fp_pos)

   return token
# ------------------------------------------------------------------------------

def is_logical_op_or_attr(fp, ch):
   symbol = ch
   lexeme = symbol
   token = {}

   if lexeme in grammar.LOGIC_OP:
      token = {'token': "<op_log;%s>" % (lexeme)}

   if lexeme == '=':
      token = {'token': "<attr;%s>" % (lexeme)}

   fp_pos = fp.tell()
   lexeme += fp.read(grammar.CHAR)

   if symbol in grammar.FORBIDDEN:
      return {'error': error.FORBIDDEN_SYMBOL % (symbol)}

   if lexeme in grammar.LOGIC_OP:
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

   if symbol == grammar.SINGLEQUOTE:
      symbol = fp.read(grammar.CHAR)
      lexeme += symbol

      symbol = fp.read(grammar.CHAR)
      if not symbol == grammar.SINGLEQUOTE:
         return {'error': error.BIG_CHAR}
      else:
         lexeme += symbol

      token = {'token': "<%s;char_value>" % (lexeme)}

   else:
      symbol = fp.read(grammar.CHAR)
      if symbol == grammar.DOUBLEQUOTE:
         return {'error': error.EMPTY_STRING}

      while True:
         symbol = fp.read(grammar.CHAR)
         lexeme += symbol
         if symbol == grammar.DOUBLEQUOTE:
            token = {'token': "<%s;str_value>" % (lexeme)}
            break

   return token
# ------------------------------------------------------------------------------

def get_token(fp):
   skip_blank(fp)
   symbol = fp.read(grammar.CHAR)
   token = {}

   if symbol in grammar.QUOTES:
      token = is_string_char_value(fp, symbol)

   # not part 
   if symbol in grammar.FORBIDDEN:
      token = {'error': error.FORBIDDEN_SYMBOL % (symbol)}

   if symbol.isalpha():      
      token = is_alpha(fp, symbol)

   elif symbol.isdigit():
      token = is_digit(fp, symbol)

   elif symbol in grammar.ARIT_OP:
      token = is_arithmetic_op(fp, symbol)

   elif symbol in grammar.LOGIC_OP or symbol == '=':
      token = is_logical_op_or_attr(fp, symbol)

   elif symbol in grammar.SPEC_CHAR:
      token = is_special_char(fp,symbol)

   elif symbol == grammar.NEWLINE:
      token = {'eof': 'eof'}

   skip_blank(fp)
   return token

