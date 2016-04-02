#!/bin/bash

MISSING_END_COMMENT = \
"\nLexical error @ line %d: \n\
Have you closed your comment, lad?\n"

IDENTIFIER_EOF = \
"\nLexical error @ line %d: \n\
EOF reached when reading an identifier, check \
this, buddy!\n"

FORBIDDEN_SYMBOL = \
"\nLexical error @ line %d: \n\
\'%c\' is not part of the alphabet, champz!\n"

ID_OR_NUMBER = \
"\nLexical error @ line %d:\n\
Sorry, but there is a char inside your number \
or your identifier starts with a number, pal!\n"

EXTRA_DOTS_NUMBER = \
"\nLexical error @ line %d:\n\
Take a look, maybe you have a few extra dots \
inside a number, bro!\n"

DOT_WITHOUT_NUMBER = \
"\nLexical error @ line %d:\n\
Don't forget: if you have a '.', you must have \
more numbers, mate!\n"

BIG_CHAR = \
"\nLexical error @ line %d:\n\
I think your char is a little big, chap!\n"

EMPTY_STRING = \
"\nLexical error @ line %d:\n\
It is sad but you must have something inside double \
quotes, sir!\n"

UNKNOWN = \
"\nLexical error @ line %d:\n\
You got me, friend! I don't know what happened...\n"
