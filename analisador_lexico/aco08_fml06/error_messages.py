#!/bin/bash


MISSING_END_COMMENT = 'Lexical error: Have you closed your comment, lad?'
IDENTIFIER_EOF      = 'Lexical error: EOF reached when reading an identifier, check this, buddy!'
FORBIDDEN_SYMBOL    = "Lexical error: \'%c\' is not part of the alphabet, champz!"
ID_OR_NUMBER        = "Lexical error: Sorry, but there is a char inside your number or your identifier start with a number, pal!"
EXTRA_DOTS_NUMBER   = "Lexical error: Take a look, maybe you have a few extra dots inside a number, bro!"
DOT_WITHOUT_NUMBER  = "Lexical error: Don't forget: if you have a '.', you must have more numbers, mate!"
BIG_CHAR            = "Lexical error: I think your char is a little big, chap!"
EMPTY_STRING        = "Lexical error: It is sad but you must have something inside double quotes, sir!"
