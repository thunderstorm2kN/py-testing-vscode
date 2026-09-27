#This is 2nd part of 1st chapter of the book Think Python.

integer_a = 5  ;  print("This is an integer: " + str(integer_a)) # 5

#This is a float: a number with a decimal point.

#Python can check the type of a variable using the type() function.
print("Type of variable a: " + str(type(integer_a)))

float_b = 5.0
print("Type of variable b: " + str(type(float_b)))
 
string_c = "This is a string"
print("Type of variable c: " + str(type(string_c)))



#Variables can be reassigned to different types of values.

#These get rounded down  when data types(like float() ) are used as functions to 
# convert values from one type to another.

float_a = 5.8 # Function int() rounds down the float to the nearest integer.
print("This float is converted to a integer: " + str(int(float_a))) 

int_b = 5     # Function float() converts the integer to a float. 
                # We still need str() to print the float as a string and concatenate it to the string. 
print("This integer is converted to a float: " + str(float(int_b))) 


#Even more interesting is that even numbers between `` will result in a string.
string_d = "  '5.8' " # This will be a string, not a float.
print("This seemengly float is actually a string: " + str(type(string_d))) 

#   This is commented because it will result in an error.
# print("Strings cant work with numbers:" + str(string_d) + 4)

#Strings also can be converted to floats using the float() function.
string_e = "58"
print("This string will get converted to a float: " + str(float(string_e)))



# For larger integer numbers we cant use commas to separate the digits. 
# Python will throw an error if we do that.

Large_integer = 1,000,000 # This will throw an error.
print("This is a tuple instead of a large integer: " + str(Large_integer)) 
# This will result in (1, 0, 0) because of the commas. Python will treat it as a tuple.

Correct_Large_integer = 1_000_000 # This is the correct way to write a large integer.
print("This is a correct large integer: " + str(Correct_Large_integer))


#Left at Glossary, pg 25