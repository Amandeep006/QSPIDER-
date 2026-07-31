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

# year=int(input("Enter the year : "))
# if year%4==0 and year%100!=0:
#     print(f"The given {year} year is leap year")
# elif year%400==0:
#     print(f"The given {year} is a leap year")
# else:
#     print(f"The given {year} is not a leap year")



"""WAPT CREATE A CALCULATOR TO PERFORM OPERATIONS LIKE +,-,*,/"""
# a=int(input("Enter the first number : "))
# b=int(input("Enter the second number : "))
# print("Choose one operations : +, - , *, / ")
# chose=input("Enter your operational Symbol : ")
# if chose=="+":
#     print(f"Addition of both the number {a+b}")
# elif chose=="-":
#     print(f"Subtraction of both the number {a-b}")
# elif chose=="*":
#     print(f"Multiplication of both the number {a*b}")
# elif chose=="/":
#     print(f"Division of both the number {a/b}")
# else:
#     print(f"You are not choice any symbol")



"""WAPT TAKE A STUDENT PERCENTAGE AS INPUT AND DETERMINE THE GRADE BASED ON THE FOLLOWINF GIVEN CONDITION."""
# 90 and above =A
# 75-89 = B
# 60-74=C
# 40-59=D
# below 40 =FAIL

# per=float(input("Enter your percentage : "))
# if per>=90:
#     print(f"Grade A")
# elif per >=75:
#     print("Grade B")
# elif per >=60:
#     print("Grade C")
# elif per>=40:
#     print("Grade D")
# else :
#     print("You are fail")


"""WAPT DETERMINE THE  AGE GROUP OF A PERSON BASED ON A GIVEN BELOW CONDITION."""
# AGE                   OUTPUT
# 60 AND ABOVE  -  ADULT
# 20 TO 59      -  TEENAGE
# BELOW 12      -  CHILD

# age=int(input("Enter your age : "))






""" WAPT TAKE A NUMBER (1-7) AS INPUT AND DISPLAY THE  CORRESPONDING DAY OF THE WEEK."""
# print("Choise the number from 1 to 7 : ")
# n=int(input("Enter your choice : "))
# if n==1:
#     print("Monday")
# elif n==2:
#     print("Tuesday")
# elif n==3:
#     print("Wednesday")
# elif n==4:
#     print("Thursday")
# elif n==5:
#     print("Friday")
# elif n==6:
#     print("Saturday")
# elif n==7:
#     print("Sunday")
# else:
#     print("Your choice is incorrect")


"""WAPT CALCULATE THE TAX BASED ON THE SALARY."""
# above 20lak 30%
# above 15lak 15%
# above 12lak 10%
# below 12lak No tax 

# sal =int(input("Enter your salary : "))
# if sal>=2000000:
#     print(f"Tax Payable : {((sal-2000000)*30)/100 + ((sal-1500000)*15)/100 + (sal*10)/100}")
# elif sal>1500000:
#     print(f"{((sal-1500000)*15)/100 + (sal*10)/100}")
# elif sal> 1200000:
#     print(f"Tax Payable : {(sal*10)/100}")

# else :
#     print(f"Your {sal} is 12Lakh or below, So You don't need to pay tax. ")



"""WAPT TO CHECK WHETHER A GIVEN CHARACTER IS VOWELS OR CONSONANT """
# ch=input("Enter any character : ")
# if ch.isalpha():
#     if ch in "AEIOUaeiou":
#         print(f"The given character '{ch}' is vowel.")
#     else :
#         print(f"The given  character '{ch}' is consonant.")

# else:
#     print(f"The given character '{ch}' is not a alphabet")


"""WAPT THAT TAKES AGE AND INCOME HAS INPUT AND BASED ON THE GIVEN BELOW CONDITION  CHECK WHETHER PERSON IS ELIGIBLE TO LOAN OR NOT.
1. AGE SHOULD ABOVE 21 
2. IF AGE IS ABOVE 21 THEN CHECK IF INCOME IS MORE THAN 30K PER MONTH THEN ELIGIBLE FOR LOAN.
3. 
"""

# age=int(input("Enter your age : "))
# income =int(input("Enter your income : "))

# if age >21:
#     if income >30000:
#         print("You are eligible for loan.")
#     else:
#         print("Your income is too low for the loan.")

# else:
#     print("Your age is to minimum.")

""" WAPT CALCULATE THE BONUS OF AN EMPLOYEE USING NESTED IF STATEMENT. 
THE COMPANY HAS FOLLOWING RULES :
1. IF THE EMPLOYEE HAS 5 OR MORE YEARS OF EXPERIENCE AND IF THE EMPLOYEE SALARY IS LESS THAN 50K THEN EMPLOYEE WILL GET BONUS OF 10K OTHERWISE 5K.
2. IF EMPLOYEE HAS LESS THAN 5 YEARS OF EXPERIENCE, THE EMPLOYEE IS NOT ELIGIBLE FOR A BONUS.
"""
# sal=int(input("Enter your salary : "))
# exp=int(input("Enter your workine experience : "))
# if exp>5:
#     if sal>50000:
#         print("The employee get 10k bonus.")
#     else:
#         print("The employee does not get bonus.")

# else:
#     print("The employee is not eligible for a bonus.")


"""WAPT CALCULATE THE GRADE OF A STUDENT USING NESTED-IF STATEMENT.
1. IF STUDENT'S MARKS ARE 35 OR ABOVE , STUDENT IS PASS .
   A.  IF MARKS ARE 90 TO 100 PRINT GRADE 'A'.
   B.  ELSE-IF MARKS ARE 75 TO 89 PRINT GRADE 'B'.
   C.  ELSE-IF MARKS ARE 60 TO 74 PRING GRADE 'C'.
   D.  OTHERWISE PRINT GRADE 'D'.

2. IF STUDENTS MARKS ARE BELOW 35 PRINT FAIL.
"""

# marks=int(input("Enter Your Marks : "))
# if marks>35:
#     if marks >=90:
#         print("Grade A")
#     elif marks>=75:
#         print("Grade B")
#     elif marks >=60:
#         print("Grade C")
#     else :
#         print("Grade D")
# else:
#     print("You are fail.")




