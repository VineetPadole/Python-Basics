#String methods

#len
#It counts the numbers of characters and also the space
# Syntax: len(variable) 
#Ex :- 
name = input("Enter your full name:")
print(len(name))  #O/P : Vineet Padole  #O/P :  13

#find
#It finds the character and gives the index as a result
#If the character can not be found it will give -1 as a output 
# Syntax: 1.variable.find("Character") #This will only find the first occurrence 
#      2.variable.rfind("Character") #This will only find the last occurrence
#1.Ex :- 
name = input("Enter your full name:")
print(name.find("q"))
#I/P : Vineet Padole  #O/P : 6
#2.Ex :-
name = input("Enter your full name:")
print(name.rfind(" "))
#I/P : Vineet Padole ni  #O/P : 13
#3.Ex :- 
name = input("Enter your full name:")
print(name.find("q"))
#I/P : Vineet Padole  #O/P : -1

#capitalize
#It capitalizes the first letter 
# Syntax:-
variable.capitalize()
#Ex :-  
name = input("Enter your full name: ")
print(name.capitalize())
#I/P :  vineet padole  #O/P : Vineet padole

#upper
#All the letters will be upper case
# Syntax: variable.upper()
#Ex :- 
name = input("Enter your full name: ")
print(name.upper())
#I/P :  vineet padole  #O/P : VINEET PADOLE

#lower
#All the letters will be lower case
# Syntax: variable.lower()
#Ex :- 
name = input("Enter your full name: ")
print(name.lower())
#I/P :  VINEET PADOLE  #O/P : vineet padole

#isdigit
#All the character should be digits only
#If all the characters are digit the output will be boolean value 
#If their is a space then output wil be False
# Syntax: name.isdigit()
#Ex :- 
name = input("Enter your username: ")
print(name.isdigit())
#I/P : nigga123 #O/P : False
#Ex :- 
name = input("Enter your username: ")
print(name.isdigit())
#I/P : 123 #O/P : True

#isalpha
#All the character should be alphabets only
#If all the characters are digit the output will be boolean value 
#If their is a space then output wil be False
# Syntax: name.isalpha()
#Ex :- 
name = input("Enter your username: ")
print(name.isalpha())
I/P : nigga123 #O/P : False
#Ex :- 
name = input("Enter your username: ")
print(name.isalpha())
#I/P : nigga #O/P : True

#count
#It counts the number of characters
# Syntax: variable.count("character")
#Ex :- 
name = input("Enter your full name: ")
print(name.count("e"))  #Means it is caps sensitive 
#I/P :  Vineet Padole  #O/P : 3

#replace
#It will replace a with a desired character
#It can also be replaced with empty string
# Syntax: variable.replace("The character want to replace" , "The character want to be replaced with")
#Ex :- 
name = input("Enter your full name: ")
print(name.replace(" ","_"))
#I/P : Vineet Padole #O/P : Vineet_Padole
#Ex :- 
name = input("Enter your full name: ")
print(name.replace(" ",""))
#I/P : Vineet Padole #O/P : VineetPadole



#string indexing
#Accessing elements of a sequence using [] (indexing operators) [start : end :step]
# Syntax: variable[start : end :step] #start : slice begins, end : slice end (excluding), step : The "jump" or interval
#Ex :- 
credit_number = "1234-5678-9012-3456"
print(credit_number[1]) #O/P : 2
print(credit_number[0 : 4]) #O/P : 1234
print(credit_number[: 4]) #O/P : 1234 #If the start is not specified it will start from the beginning
print(credit_number[5 : 9]) #O/P : 5678
print(credit_number[5:]) #O/P : 5678-9012-3456 #It will assume everything after the start index
print(credit_number[-1]) #O/P : 6 #(-)ve number starts from the end of the string
print(credit_number[::2]) #O/P : 13-6891-46 #print every 2nd number
print(credit_number[::-1]) #O/P : 6543-2109-8765-4321 #Classic way to write string in reverse
