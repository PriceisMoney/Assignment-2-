# We will found a number is even or odd given by the user with the help of modulus operator %

num = int(input("Enter a number: ")) #take input from the user and convert it into integer and store it in num variable
if num % 2 == 0:   #checking the number is divisible by 2 or not
    print("The Given Value: Even")  #if the condition is true then print even   
else:
    print("The Given Value: Odd")   #if the condition is false then print odd   



""" Sir I have a another logic
    If 11 / 2 = 5.5 print (this is float)
    and 11 // 2 = 5 without decimal value (this is int)
    then if I subtract 11/2 - 11//2 = (0.5) if this value is equal to zero then the given value is Even else Odd
"""

# number = int(input("Enter a number: "))

# if (number / 2) - (number // 2) == 0:
#      print('The Given Value: Even')
# else:
#      print('The Given Value: Odd')

     
# Another Logic to find Even or Odd

# number1 = int(input("Enter a number: "))    
# number2 = str(number1)    #converting int to str

# if number2[-1] in ['0', '2', '4', '6', '8']:   #checking last digit
#     print('The Given Value: Even') 
# else:
#     print('The Given Value: Odd')
    

