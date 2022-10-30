"""
In this section we will see the program of Prime number:
_________________________________________________________
question : write a program to find whether the number is prime or not
_______________________________________________________________________
approach : first take a number input from user
           second check if the number is smaller than 2 than the number is not a prime number.
           else check the range of the number between one and ten if it is divisible by this number and reminder is 0
           then it is not a prime number :
           esle it is a primer number.
"""
A = int (input("Enter the number: "))
if(A < 2):
    print("The number is not a prime number")
else:
    for i in range(2 , A):
        if (A % i == 0):
            print("Number is not a prime number.")
            break
        else:
            print("Number is prime number.")