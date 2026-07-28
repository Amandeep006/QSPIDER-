""" Write a program to few statement in python."""
# print("Hello world\nWe love to code\nPython is easy to learn\nPrint byy byy ")

""" WAPT add two numbers."""
# a=int(input("Enter the first number :"))
# b=int(input("Enter the second number : "))
# print(f"The sum of both the number is {a+b}")


"""WAPT SQUARE THE GIVEN NUMBER"""
# n=int(input("Enter the number :"))
# print(f" The square of the given number {n**2}")

""" WAPT CALCULATE THE SQUARE ROOT OF A GIVEN NUMBER."""
# import math 
# n=int(input("Enter the number :"))
# print(f"The square root of the given number is {int(n**0.5)}")
# # we can also use math library for finding the square of the number:  math.sqrt(25) and also cubeic root: math.cbrt(27)
# print(f"The  square root of the given number is {int(math.sqrt(n))}")


""" WAPT CALCULATE THE CUBE OF A GIVEN NUMBER."""
# n=int(input("Enter the number "))
# print(f"Cubic of number : {n**3}")



"""WAPT CALCULATE AREA OF TRIANGLE """
# base=int(input("Enter the base of the triangle :"))
# height=int(input("Enter the height of the triangle :"))
# print(f"Area of the triangle {0.5*base*height}.")

""" WAPT CALCULATE SIMPLE INTEREST FOR A GIVEN PRINCIPLE AMMOUNT , RATE OF INTEREST AND TIME PERIOD. COLLECT ALL THIS FROM USER. """
# principle=float(input("Enter your ammount : "))
# rate=float(input("Enter your rate of interest :"))
# time=float(input("Enter the time period in years : "))
# print(f"Simple interest of the user is {(principle*rate*time)/100}")


"""WAPT CONVERT CELCIUS INTO FREHANITE. """

# n=float("Enter the temperature in celcius : ")


"""WAPT SWAP THE VALUE OF A VARIABLE USING TWO VARIABLE"""
# a=int(input("Enter the X value :"))
# b=int(input("Enter the Y value :"))
# print(f"Before Swapping : a ={a} and b ={b}.")
# a,b=b,a
# print(f"After Swapping : a ={a} and b ={b}.")

# without multiplt assigning 
# a=a+b
# b=a-b
# a=a-b

# a=a*b
# b=a/b
# a=a/b



# print(f"After Swapping : a ={a} and b ={b}.")


"""WAPT SWAP THE VALUES OF A VARIABLE USING THREE VARIABLE"""
# a=int(input("Enter the X value :"))
# b=int(input("Enter the Y value :"))
# print(f"Before Swapping : a = {a} and b = {b}.")
# temp=a
# a=b
# b=temp
# print(f"After Swapping : a = {a} and b = {b}.")


"""WAPT CONVERT DECIMAL INTO BINARY, OCTOR AND HEXADECIMAL NUMBER"""
# num=int(input("Enter the number : "))
# print(f"Binay number : {bin(num)[2:]}")
# print(f"Hexdecimal number : {hex(num)[2:]}")
# print(f"Octant number : {oct(num)[2:]}")

""" WAPT CHECK WHETHER A GIVEN NUMBER IS EVEN OR NOT , IF IT IS EVEN THEN SQUARE THE NUMBER. """
# num=int(input("Enter the number : "))
# if num%2==0:
#     print(f"Square of number : {num**2}")

# else:
#     print("It is not a even number")


"""WAPT CHECK WHETHER A GIVEN NUMBER IS ODD OR NOT, IF IT IS ODD THEN CUBE THE NUMBER. """
# num=int(input("Enter the number :"))
# if num%2!=0:
#     print(f"cubic of number : {num**3}")

""" WAPT CHECK WHETHER A GIVEN CHARACTER IS ALPABHENT OR NOT , IF IT IS ALPHABET THEN PRINT HELLO WOROLD """

# str=input("Enter any world : ")
# # if str.isalpha():
# if "A"<=str<="Z" or "a"<=str<="z":
#     print("Hello World ")

"""wapt a given check is upper case or not, if it is upper case then print that charcter."""

# str=input("Enter any words: ")
# if str.isupper():
#     print(f"Given string : {str}")


"""wapt to check whether a given number is divisible by both 3 and 7 or not, if it is divisible by both then print number is divisible by both.is""" 
# num=int(input("Enter any number : "))
# if num%3==0 and num%7==0:
#     print(f"Number is divisible by 3 and 7 are {num/3} and {num/7} respectively. ")

"""WAPT CHECK WHETHER GIVEN NUMBER IS EVEN OR ODD."""
# num=int(input("Enter the any number : "))
# if num%2==0:
#     print(f"The given number {num} is even")
# else:
#     print(f"The given number {num} is odd.")


"""WAPT CHECK WHETHER A GIVEN NUMBER IS EVEN OR ODD, IF IT IS EVEN THEN SQUARE THE NUMBER AND IF IT ODD THEN CUBE THE NUMBER """

# num=int(input("Enter the any number : "))
# if num%2==0:
#     print(f"")
# else:
#     print(f"The given number {num} is odd.")


"""WAPT CHECK WHETHER A GIVEN CHARACTER IS VOWEL OR NOT """
# vowels=["a","e","i","o","u","A","E","O","I","U"]
# str=input("Enter any character : ")
# if str in vowels :
#     print(f"The given character {str} is vowels.")

# else:
#     print(f"The given character {str} is not vowels.")


"""WAPT CHECK WHETHER A GIVEN CHARACTER CONSONANAT OR NOT."""

# vowels=["a","e","i","o","u","A","E","O","I","U"]
# str=input("Enter any character : ")
# if str not in vowels and str.isalpha() :
#     print(f"The given character '{str}' is Consonant.")

# else:
#     print(f"The given character '{str}' is not Consonant.")



"""WAPT FIND THE LARGEST BETWEEN TWO NUMBERS"""
# a=int(input("Enter the first number : "))
# b=int(input("Enter the second number : "))
# if a>b:
#     print(f"{a} is greater than {b}.")
# else:
#     print(f"{b} is grater than {a}.")


"""WAPT FIND THE SMALLEST BETWEEN TWO NUMBERS."""
# a=int(input("Enter the first number : "))
# b=int(input("Enter the second number : "))
# if a<b:
#     print(f"{a} is lower than {b}.")
# else:
#     print(f"{b} is lower than {a}.")

"""WAPT CHECK THE GIVEN NUMBER IS OFF THREE DIGIT OR NOT"""
# num=int(input("Enter any number :"))
# if num>=100 and num<=999:
#     print(f"{num} has three digit")
# else:
#     print(f"The num has no three digit.")


"""WAPT CHECK WHETHER A GIVEN STRING IS PALINDROME OR NOT."""
# str=input("Enter any string : ")
# if str==str[::-1]:
#     print(f"The given string '{str} is Palindrome.'")
# else:
#     print(f"The given string '{str} is not Palindrome.'")


"""WAPT CHECK WHETHER A GIVEN NUMBER IS POSITIVE, NEGATIVE OR ZERO."""
# num=int(input("Enter any number : "))
# if num>0:
#     print(f"The given number {num} is positive.")
# elif num<0:
#     print(f"The given number {num} is negative number.")
# else:
#     print(f"The given number {num} is zero.")


"""WAPT FIND THE LARGEST AMONG THREE NUMBERS."""
# a=int(input("Enter the first number : "))
# b=int(input("Enter the second number : "))
# c=int(input("Enter the third number : "))

# if a>b and a>c:
#     print(f"{a} is greater than {b} and {c}.")
# elif b>a and b>c:
#     print(f"{b} is greater than {a} and {c}")
# else:
#     print(f"{c} is greater than {a} and {b} ")                                                                                                

"""WAPT FIND THE SMALLEST AMONG THREE NUMBERS."""
"""WAPT CHECK WHETHER A GIVEN YEAR IS LEAP YEAR OR NOT."""