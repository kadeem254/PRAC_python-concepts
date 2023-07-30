######################################################################
# Python supports the followign data types in built:
# - Text Type:	str
# - Numeric Types:	int, float, complex
# - Sequence Types:	list, tuple, range
# - Mapping Type:	dict
# - Set Types:	set, frozenset
# - Boolean Type:	bool
# - Binary Types:	bytes, bytearray, memoryview
# - None Type:	NoneType
######################################################################

######################################################################
# GETTING A VALUE'S TYPE
# Done using the type() function
######################################################################

num_a = 255
print( "num_a is of type ", type(num_a) )

######################################################################
# TYPE EXAMPLES
# Giving examples of the different types by assign values to them
######################################################################

type_str        = "Apples and Bananas"
type_int        = 2000
type_float      = 3.1415
type_complex    = 1j
type_list       = [ "apples", "and", "bananas" ]
type_tuple      = ( "apples", "and", "bananas" )
type_range      = range( 0, 30, 2 )
type_dict       = { "first name": "Jimmy", "last name": "Neutron" }
type_set        = { "apples", "and", "bananas" }
type_frozenset  = frozenset({ "apples", "and", "bananas" })
type_bool       = True
type_bytes      = b"Hello"
type_bytearray  = bytearray( 5 )
type_memoryview = memoryview( bytes(5) )
type_none       = None

