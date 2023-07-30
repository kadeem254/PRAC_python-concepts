
######################################################################
# VARIABLES
# - are used to store values that are of use to the user
# - They allow the user to easily access a reused value without making
#   many mistakes.
######################################################################

num_1 = 10;
num_2 = 23;

print( "num_1(10) + num_2(23) = " + str(num_1 + num_2) ) # prints 33

######################################################################
# CASTING
# This is done to specify the data type of the variable.
######################################################################

num_3 = int( 17 ) # read as 17
word_1 = str( 17 ) # read as '17'
float_1 = float( 17 ) # read as 17.0

print( 'num_3 => ' + str(num_3) )
print( 'word_1 => ' + word_1 )
print( 'float_1 => ' + str(float_1) )

######################################################################
# MANY VALUES TO MULTIPLE VARIABLES
# You can easily assign values to multiple values on the same
# declaration.
######################################################################

num_4, word_2, float_2 = 48, "Bazinga", 4.567

# store the output using a variable to make it easier to manage.
msg = "num_4 = " + str(num_4) + ", "
msg += "word_2 = '" + word_2 + "', "
msg += "float_2 = " + str(float_2)

print( msg )

######################################################################
# ONE VALUE TO MULTIPLE VARIABLES
# Gives multiple variables the same value
######################################################################

word_3 = word_4 = word_5 = "Bird"

msg = "Values of word 3, 4 and 5 are: "
msg += word_3 + ", " + word_4 + ", " + word_5

print( msg )

######################################################################
# UNPACK A COLLECTION
# Python allows you to extract the values of a list or tuple into
# variables, this is called unpacking.
######################################################################

num_list_1 = [ 23, 34, 56 ]
num_5, num_6, num_7 = num_list_1

print( num_5 )
print( num_6 )
print( num_7 )

######################################################################
# VARIABLE SCOPE
# - Global => These are available to all code blocks within a script
# - Local => These are only accessible within the code block or
#   Function in which they are defined.
######################################################################

global_num = 32

def showLocalScope():
    global_num = 128
    print( "local scope:", global_num )
    return

showLocalScope()
print( "global scope:", global_num )

######################################################################
# GLOBAL KEYWORD
# - They allow creating a global variable using the 'global' keyword
######################################################################

def createGlobalVariable():
    global global_num_2
    global_num_2 = 256

createGlobalVariable()
print( "Value of assigned global: ", global_num_2 )