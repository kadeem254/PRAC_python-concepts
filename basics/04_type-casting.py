######################################################################
# TYPE CASTING
# This involves specifying a type on a variable.
######################################################################

######################################################################
# str( object, encoding, errors )
# - returns the string representation of a given object.
# - takes three parameters:
#   - object -> whose string representation is desired
#   - encoding -> e.g UTF-8, ASCII, etc
#   - errors -> a response when decoding fails
######################################################################

age = str(24)
print( age )

invalid = bytes( 'pythön', encoding='utf-8' )
print( str( invalid, encoding="ascii", errors="ignore" ) )

# print( str( invalid, encoding="ascii", errors="strict" ) )
# 
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in
# position 4: ordinal not in range(128)
