#!/usr/bin/python

# FAZER ESSAS COISAS AQUI CAPSLOCK
DELIMITER  = [' ', '\t', '\n', '(', ')', '{', '}', ';']

DATA_TYPE  = ['int', 'char', 'float', 'const', 'string']
SPEC_CHAR  = ['{', '}', '[', ']', '(', ')', ';']
ARIT_OP    = ['+', '++', '-', '--', '*', '/', '#']
LOGIC_OP   = ['>', '<', '>=', '<=', '==', '!', '!=']
RESERVED   = ['for', 'while', 'do', 'if', 'else', 'main']

FORBIDDEN  = ['@', '$', '`', ',']

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

# token keys
COMMENT = 'comment'
TOKEN   = 'token'
ERROR   = 'error'
EOF     = 'eof'

CHAR = 1
