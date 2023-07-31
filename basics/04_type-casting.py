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

# integer
print( "integer => str(20): ", str(20) )
# float
print( "float => str(20.00): ", str(20.00) )
# complex
print( "complex => str(2+4j): ", str( 2 + 4j ) )

# list
print( "list => str( [20,'Twenty'] ): ", str( [20,'Twenty'] ) )
# tuple
print( "tuple => str( (20,'Twenty') ): ", str( (20,'Twenty') ) )
# range
print( "range => str( range(0,10,2) ): ", str( range(0,10,2) ) )
# dictionary
print( "dict => str( {'name': 'Alexander', 'age': 24} ): ", str({'name': 'Alexander', 'age': 24}) )

# set
print( "set => str( {'20','Twenty'} ): ", str( {'20','Twenty'} ) )
# frozenset
print( "frozenset => str( frozenset({20,'Twenty'}) ): ", str( frozenset({20,'Twenty'}) ) )

# boolean
print( "bool => str(True): ", str(True) )

# bytes
print( "bytes => str( bytes('python', encoding='ascii') ): ", str( bytes('python', encoding='ascii') ) )
# bytearray
print( "bytearray => str( bytearray(5) ): ", str( bytearray(5) ) )

# memoryview
print( "memoryview => str( memoryview(bytes(5)) ): ", str( memoryview(bytes(5)) ) )

# None
print( "none => str( None ): ", str( None ) )

# bytes - special characters
invalid = bytes( 'pythön', encoding='utf-8' )
print( str(invalid, encoding="ascii", errors="ignore") )

# utf-8 does not support ö and so will throw an error in strict mode
try:
    print( str( invalid, encoding="ascii", errors="strict" ) )
except UnicodeDecodeError:
    err_msg = "ö is not supported."
    print( err_msg )

# skip one line
print( "\r" )

######################################################################
# int( value, base[optional] )
# converts a number or a string to its equivalent integer
######################################################################

# float
print( "from float => int(9.9): ", int(9.9) )
# string
print( "from string => int('9'): ", int('9') )
# binary
print( "from binary => int(0b1101): ", int( 0b1001 ) )
# octal
print( "from octal => int(0o11): ", int(0o11) )
# hexadecimal
print( "from hexadecimal => int(0x9): ", int(0x9) )

# skip one line
print( "\r" )
