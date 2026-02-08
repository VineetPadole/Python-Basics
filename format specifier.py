#format specifiers
#format a value based on what flags are inserted
# Syntax: {value:flags}

price1 = 3.14159
price2 = -987.65
price3 = 12.34

price1_ = 3000.14159
price2_ = -9870.65
price3_ = 1200.34

# . (number)f = round to that many decimal places (fixed point)
print(f"Price 1 is {price1:.2f}") #O/P : 3.14 #This will print 2 numbers after decimal 
print(f"Price 2 is {price2:.1f}") #O/P : -987.65 #This will print 1 number after decimal  
print(f"Price 3 is {price3:.3f}") #O/P : 12.340 #This will print 3 numbers after decimal #It will concatenate 0 if a number doesn't  

# : (number) = allocate that many spaces
print(f"Price 1 is {price1:10}") #O/P :|   3.14159 }  
print(f"Price 2 is {price2:10}") #O/P :|   -987.65 } #This will add spaces till the end of the string
print(f"Price 3 is {price3:10}") #O/P :|     12.34 }

# :03 = allocate and zero pad that many spaces
print(f"Price 1 is {price1:010}") #O/P :0003.14159  }
print(f"Price 2 is {price2:010}") #O/P :-000987.65  } #This will add 0's to the padded space
print(f"Price 3 is {price3:010}") #O/P : 0000012.34 }

# :‹ = left justify
print(f"Price 1 is {price1:<10}") #O/P :3.14159   | }
print(f"Price 2 is {price2:<10}") #O/P :-987.65   | } #This will left justify everything and leave space to the right till the end of the string  
print(f"Price 3 is {price3:<10}") #O/P :12.34     | }

# :› = right justify
print(f"Price 1 is {price1:>10}") #O/P :|   3.14159| }  
print(f"Price 2 is {price2:>10}") #O/P :|   -987.65| } #This will right justify everything and leave space to the left till the end of the string 
print(f"Price 3 is {price3:>10}") #O/P :|     12.34| }

# :^ = center align
print(f"Price 1 is {price1:^10}") #O/P :| 3.14159 | }        
print(f"Price 2 is {price2:^10}") #O/P :| -987.65 | } #This will center align everything leaving spaces before and after the number if needed 
print(f"Price 3 is {price3:^10}") #O/P :|  12.34  | }
