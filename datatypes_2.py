# Strings and Values plus types: 
#This is 2nd part of 1st chapter of the book Think Python.


#Strings are sequences of letters. 

# They can be enclosed in single quotes (' ') or double quotes (" ").
from tokenize import String


String_1 = 'We are using single quotes'
print(String_1)
String_2 = " \nWe are using double quotes\n"
print(String_2)

#Strings can also contain characters like numbers,
#punctuation, and whitespace.
String_3 = "This is a string w/ 123 & punctuation !?"
print(String_3)
#Double quotes are useful when writing with apostrophes in the string.
String_6 = "This string contains an apostrophe: It's a beautiful day!" 
print(String_6)

#Strings can also contain spaces and numbers.
String_7 = "This string contains  spaces  "
String_8 = " and numbers: 456 123 789"
print(String_7+String_8)


#Strings can be concatenated using the + operator.
String_4 = "\nWE are concatenating strings: \n" + String_1 + " " + String_2
print(String_4)



#The * operator can be used to repeat a string multiple times.
Looping_String = "We are looping"
String_5 = "This string gets looped 3 times:\n" + Looping_String * 3
print(String_5)


#The Len function can be used to find the length of a string.
String_9 = "Ana pare rece"     
                     #13 bcz it included the spaces between the words.
String_Length = len(String_9 )

print("The length of the string is: " + str(String_Length))
    # You transform the integer into a string using str() function,
    #Not to get error when concatenating a string with an integer.


