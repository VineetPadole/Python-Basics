#while loop
#Execute some code WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ") #If we would have nave not taken a input the loop will run infinitely 
print(f"Hello {name}")
I/P : 
O/P : You did not enter your name
     Enter your name: Vineet
     Hello Vineet
