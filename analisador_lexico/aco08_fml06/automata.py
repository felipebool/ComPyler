#!/usr/bin/python

import grammar as grammar
import error_messages as error

line = 1

def skip_blank(fp):
   symbol = fp.read(grammar.CHAR)
   global line

   while True:
      if not symbol.isspace():
         fp.seek(fp.tell() - 1)
         break
      elif symbol == grammar.NEWLINE:
         line += 1
         
      symbol = fp.read(grammar.CHAR)
# ------------------------------------------------------------------------------


def skip_comment(fp):
   window = fp.read(grammar.CHAR)
   global line

   while True:
      symbol = fp.read(grammar.CHAR)

      if symbol == grammar.NEWLINE:
         line += 1

      if len(symbol) == 0:
         return {grammar.ERROR: error.MISSING_END_COMMENT % (line)} 

      window += symbol

      if window == grammar.OPENCOMMENT:
                 return {grammar.ERROR: error.MISSING_END_COMMENT % (line)}

      if window != grammar.CLOSECOMMENT:
         window = window[1]
      else:
         break

   return {grammar.COMMENT: grammar.COMMENT}
# ------------------------------------------------------------------------------


def is_alpha(fp, ch):
   """Return an alpha token (identifiers, reserved words and language types)"""
   global line
   symbol = ch
   lexeme = ''

   while True:
      if symbol in grammar.FORBIDDEN:
         return {grammar.ERROR: error.FORBIDDEN_SYMBOL % (line, symbol)}

      if symbol in grammar.DELIMITER:
         fp_pos = fp.tell()
         break

      if symbol in grammar.ARIT_OP or symbol == '=':
         fp_pos = fp.tell()
         break

      lexeme += symbol
      symbol = fp.read(grammar.CHAR)

   if lexeme in grammar.DATA_TYPE:
      token = {grammar.TOKEN: "<type;%s>" % (lexeme)}
   elif lexeme in grammar.RESERVED: 
      token = {grammar.TOKEN: "<reserved;%s>" % (lexeme)}
   else:
      token = {grammar.TOKEN: "<id;%s>" % (lexeme)}

   fp.seek(fp_pos - 1)
   return token
# ------------------------------------------------------------------------------


def is_digit(fp, ch):
   """Return a number token"""
   global line
   has_point = False
   symbol = ch
   lexeme = ""
   token = {}
   global line

   while True:
      if symbol in grammar.FORBIDDEN:
         return {grammar.ERROR: error.FORBIDDEN_SYMBOL % (line, symbol)}

      if symbol in grammar.DELIMITER:
         fp_pos = fp.tell()
         fp.seek(fp_pos - 1)
         break

      lexeme += symbol

      if symbol.isalpha():
         return {grammar.ERROR: error.ID_OR_NUMBER % (line)}

      if symbol == '.':
         if has_point:
            return {grammar.ERROR: error.EXTRA_DOTS_NUMBER % (line)}
         else:
            has_point = True

         fp_pos = fp.tell()
         symbol = fp.read(grammar.CHAR)

         if not symbol.isdigit():
            return {grammar.ERROR: error.DOT_WITHOUT_NUMBER % (line)}
         else:
            fp.seek(fp_pos)

      if symbol in grammar.DELIMITER:
         break

      symbol = fp.read(grammar.CHAR)
   
   token = {grammar.TOKEN: "<num;%s>" % (lexeme)}
   return token
# ------------------------------------------------------------------------------


def is_arithmetic_op(fp, ch):
   """
      Return an arithmetic token or skip comment
   """
   symbol = ch
   lexeme = symbol

   if symbol in ['*', '#']:
      token = {grammar.TOKEN: "<op_arit;%s>" % lexeme}

   if symbol in ['/', '+', '-']:
      fp_pos = fp.tell()
      lexeme += fp.read(grammar.CHAR)

      if lexeme == grammar.OPENCOMMENT:
         token = skip_comment(fp)

      if lexeme in grammar.ARIT_OP:
         token = {grammar.TOKEN: "<op_arit;%s>" % (lexeme)}

      
      if not lexeme[1] in grammar.ARIT_OP:
         token = {grammar.TOKEN: "<op_arit;%s>" % (symbol)}
         fp.seek(fp_pos)

   return token
# ------------------------------------------------------------------------------

def is_logical_op_or_attr(fp, ch):
   symbol = ch
   lexeme = symbol
   token = {}
   global line

   if lexeme in grammar.LOGIC_OP:
      token = {grammar.TOKEN: "<op_log;%s>" % (lexeme)}

   if lexeme == '=':
      token = {grammar.TOKEN: "<attr;%s>" % (lexeme)}

   fp_pos = fp.tell()
   lexeme += fp.read(grammar.CHAR)

   if symbol in grammar.FORBIDDEN:
      return {grammar.ERROR: error.FORBIDDEN_SYMBOL % (line, symbol)}

   if lexeme in grammar.LOGIC_OP:
      token = {grammar.TOKEN: "<op_log;%s>" % (lexeme)}
   else:
      fp.seek(fp_pos)
   
   return token
# ------------------------------------------------------------------------------

def is_special_char(fp, ch):
   token = {grammar.TOKEN: "<;%s>" % (ch)}
   return token
# ------------------------------------------------------------------------------

# TODO: deal with string/char without closing "|'
def is_string_char_value(fp, ch):
   symbol = ch
   lexeme = symbol
   global line

   if symbol == grammar.SINGLEQUOTE:
      symbol = fp.read(grammar.CHAR)
      lexeme += symbol

      symbol = fp.read(grammar.CHAR)
      if not symbol == grammar.SINGLEQUOTE:
         return {grammar.ERROR: error.BIG_CHAR % (line)}
      else:
         lexeme += symbol

      token = {grammar.TOKEN: "<%s;char_value>" % (lexeme)}

   else:
      symbol = fp.read(grammar.CHAR)
      if symbol == grammar.DOUBLEQUOTE:
         return {grammar.ERROR: error.EMPTY_STRING % (line)}

      while True:
         symbol = fp.read(grammar.CHAR)
         lexeme += symbol
         if symbol == grammar.DOUBLEQUOTE:
            token = {grammar.TOKEN: "<%s;str_value>" % (lexeme)}
            break

   return token
# ------------------------------------------------------------------------------

def get_token(fp):
   skip_blank(fp)
   symbol = fp.read(grammar.CHAR)
   token = {}
   global line

   if symbol in grammar.QUOTES:
      token = is_string_char_value(fp, symbol)

   elif symbol in grammar.FORBIDDEN:
      token = {grammar.ERROR: error.FORBIDDEN_SYMBOL % (line, symbol)}

   elif symbol.isalpha():      
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
      token = {grammar.EOF: line}

   else:
      token = {grammar.ERROR, error.UNKNOWN % (line)}

   skip_blank(fp)
   return token

