######################################################################
# TYPE CASTING
# This involves specifying a type on a variable.
######################################################################

def generateTitleUnderline( title ):
    try:
        _title = str( title )
        _length = len( _title )
        underline = ''
        for i in range(_length):
            underline += "-"
        
        return underline
    except:
        return None
######################################################################
# str( object, encoding, errors )
# - returns the string representation of a given object.
# - takes three parameters:
#   - object -> whose string representation is desired
#   - encoding -> e.g UTF-8, ASCII, etc
#   - errors -> a response when decoding fails
######################################################################

# title the group
title = 'str()'
print( "\n", title, "\n", generateTitleUnderline(title) )

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

# # bytes - special characters
# invalid = bytes( 'pythön', encoding='utf-8' )
# print( str(invalid, encoding="ascii", errors="ignore") )

# # utf-8 does not support ö and so will throw an error in strict mode
# try:
#     print( str( invalid, encoding="ascii", errors="strict" ) )
# except UnicodeDecodeError:
#     err_msg = "ö is not supported."
#     print( err_msg )

######################################################################
# int( value, base[optional] )
# converts a number or a string to its equivalent integer
######################################################################

# title the group
title = 'int()'
print( "\n", title, "\n", generateTitleUnderline(title) )

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

######################################################################
# float( value )
# Returns a floating point value from a number or a string.
######################################################################

# title the group
title = 'float()'
print( "\n", title, "\n", generateTitleUnderline(title) )

# string
print( "from string => float('3.1415'): ", float('3.1415') )
# int
print( "from int => float(4): ", float(4) )

######################################################################
# complex( [real, [imag] ] )
# real - real part. If real is omitted, it defaults to 0.
# imag - imaginary part. If imag is omitted, it defaults to 0.
######################################################################

# title the group
title = 'complex()'
print( "\n", title, "\n", generateTitleUnderline(title) )

# string
print( "from string => complex('5-7J'): ", complex('5-7J') )
# int
print( "from int => complex(2, -3): ", complex(2, -3) )
# int
print( "from int => complex(2): ", complex(2) )
# empty declaration
print( "empty declaration => complex(): ", complex() )

######################################################################
# list( iterable )
# iterable (optional) - an object that could be a sequence or
# collection or any iterator object
# e.g strings, tuples, sets, dictionary
######################################################################

# title the group
title = 'list()'
print( "\n", title, "\n", generateTitleUnderline(title) )

# string
print( "from string => list('Wizard'): ", list('Wizard') )
# tuple
print( "from tuple => list( (20,'Twenty','XX') ): ", list( (20,'Twenty','XX') ) )
# dictionary
print( "from dict => list({ 'f_name':'Jimmy', 'l_name':'Neutron' }): ", list({ 'f_name':'Jimmy', 'l_name':'Neutron' }) )
# set
print( "from set => list({ 10, 'Ten', 'X' }): ", list({ 10, 'Ten', 'X' }) )