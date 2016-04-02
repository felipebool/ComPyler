#!/usr/bin/python

# FAZER ESSAS COISAS AQUI CAPSLOCK
delimiters = [' ', '\t', '\n', '(', ')', '{', '}', ';']

data_type  = ['int', 'char', 'float', 'const', 'string']
spec_chars = ['{', '}', '[', ']', '(', ')', ';']
op_arit    = ['+', '++', '-', '--', '*', '/', '#']
op_logic   = ['>', '<', '>=', '<=', '==', '!', '!=']
reserved   = ['for', 'while', 'do', 'if', 'else', 'main']
separators = [';', ',']
ign_list   = [' ', '\t', '\n']

forbidden  = ['@', '$', '`']

# Few useful constants (this is more like language, but...)
NEWLINE    = '\n'
TAB        = '\t'
BLANKSPACE = ' '
BLANK      = [NEWLINE, TAB, BLANKSPACE]

SINGLEQUOTE = '\''
DOUBLEQUOTE = '\"'
QUOTES      = [SINGLEQUOTE, DOUBLEQUOTE]

OPENCOMMENT  = '/*'
CLOSECOMMENT = '*/'

CHAR = 1
