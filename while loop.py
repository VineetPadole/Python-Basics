#while loop
#Execute some code WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ") #If we would have nave not taken a input the loop will run infinitely 
print(f"Hello {name}")
#I/P : Vineet
#O/P : You did not enter your name
#     Enter your name: Vineet
#     Hello Vineet

food = input("Enter a food you like (q to quit): ")
while not food == "q": #When food is not q it will continue to run the loop but if the user puts in q then we will exit the loop  
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")
print ("bye")

# Similarly we can also use 'or' and 'and' operators
