"""WAPT PRINT YOUR NAME FIVE TIMES """
# n=0
# while(n<5):
#     print("Amandeep")
#     n+=1
    
# print("------------Another method--------------")

# while True:
#    if n==5:
#       break 
#    print("Amandeep")
#    n+=1


"""WAPT DISPLAY ALL THE NUMBERS STARTING FROM 1 TO 7."""
# n=1
# while n<=7:
#     print(n)
#     n+=1

# print("----------------")
# v=1
# while True:
#     if v==8:
#         break
#     print(v)
#     v+=1


"""WAPT PRINT ALL THE NUMBER STARTING FROM 7 TO 1."""
# n=7
# while n>=1:
#     print(n)
#     n-=1


"""WRITE A PROGRAM TO DISPLAY ALL THE EVEN NUMBER STARTING FROM 1 TO 10."""
# n=1
# while n<=10:
#     if n==1:
#         n+=1
#         continue
#     print(n)
#     n+=2 



# n=1
# while n<=10:
#     if n%2==0:
#         print(n)
#     n+=1


# for i in range(2, 11,2):
#     print(i)
    
"""WAPT DISPLAY ALL THE  ODD NUMBERS STARTING FROM 1 TO 10."""

# n=1
# while n<=10:
#     print(n)
#     n+=2


"""WAPT ALL THE NUMBERS BY TAKING RANGE FROM THE USER."""
# n1=int(input("Enter the starting number : "))
# n2=int(input("Enter the ending number : "))
# while n1<=n2:
#     print(n1)
#     n1+=1


"""WAPT ADD 5 WITH THE EVEN NUMBERS AND MULTIPLY 5 ALL THE ODD NUMBERS STARTING FROM 1 TO 7"""
# n=1
# while n<=7:
#     if n%2==0:
#         print(n+5)
#         n+=1
#     else:
#         print(n*5)
#         n+=1

"""WAPT ALL THE NUMBERS STARTING FROM 1 TO 7 IN THE GIVEN BELOW STYLE.
1 IS ODD 
2 IS EVEN 
3 IS ODD 
4 IS EVEN
"""
    
# n=1
# while n<=7:
#     if n%2==0:
#         print(f"{n} is Even.")
#     else:
#         print(f"{n} is Odd.")

#     n+=1 


"""WAPT ALL THE ALPHABETS STARTING FROM A TO Z."""
# A-Z Ascii value --> 65 to 90.
# a-z Ascii value --> 97 to 122.


"""Capital letters """
# n=65
# print("Capital letter :", end=" ")
# while n<=90:

#     print(f"{chr(n)}",end=" ") # chr() is used to print the character of ASCII value.
#     n+=1

# print(" ")
# """Small letters """
# n=97
# print("Small letter :", end=" ")
# while n<=122:
#     print(f"{chr(n)}",end=" ")
#     n+=1

# print(" ")
"""WAPT PRINT ALL THE ALPHABETS STARTING FROM Z TO A IN SMALL LETTER."""
# n=122

# print("Reverse small letter :", end=" ")
# while n>=97:
#     print(f"{chr(n)}", end=" ")
#     n-=1
   

"""WAPT TABLE OF 7."""
# i=1
# while i<=10:
#     print(f"7 X {i} : {7*i}")
#     i+=1

"""WAPT TAKE A NUMBER FROM USER AND PRINT THE TABLE OF THAT NUMBER."""
# n=int(input("Enter the number : "))
# i=10
# while i>=1:
#     print(f"{n} X {i} = { n*i}")
#     i-=1


"""WAPT TO ADD ALL THE NUMBERS STARTING FROM 1 TO 5. """
# i=1
# sum=0
# while i<=5:
#     sum+=i
#     print(i)
#     i+=1

# print(f"Sum of all numbers: {sum}")


"""WAPT TO MULTIPLY ALL THE NUMERS STARTING FROM 1 TO 5"""
# i=1
# mul=1
# while i<=5:
#     mul*=i
#     print(i)
#     i+=1

# print(f"Multiply of all numbers: {mul}")

"""WAPT ADD ALL THOSE NUMBERS WHICH ARE EVEN STARTING 1 TO 10 """
# i=1
# sum=0
# while i<=10:
#     if i%2==0:
#         sum+=i
#         print(i, end=" ")
#     i+=1

# print(f"\nSum of all the even number from 1 to 10 : {sum}")


"""WAPT MULTIPLY ALL THE ODD NUMBERS WHICH ARE PRESENT BETWEEN 5 TO 15"""
# i=5
# mul=1
# while i<=15:
#     if i%2!=0:
#         mul*=i
#         print(i, end=" ")

#     i+=1

# print(f"\nAll the odd number from 5 to 15 : {mul}")


"""WAPT COUNT HOW MANY NUMBER OF DIGITS PRESENT INSIDE A GIVEN NUMBER USING WHILE LOOP."""
# n=int(input("Enter the number : "))
# count=0
# a=n
# while n!=0:
#     count+=1
#     n//=10


# print(f"Number of digit using While : {count}")

# print(f"using len : {len(str(abs(a)))}")


"""WAPT ADD ALL THE DIGITS OF A GIVEN USIG WHILE LOOP  """
# n=int(input("Enter the number : "))
# sum=0

# # whenever you want to find the last number from the number, SO you can use num%10.
# # whenver you want to smaller the number , you can use num//10.
# while n!=0:
#     rem=n%10
#     sum+=rem
#     n=n//10

# print(f"Sum of all digits of given number : {sum}")


"""WAPT MULTIPLY ALL THE DIGIT PRESENT INSIDE THE GIVEN NUMBER . """
# n=int(input("Enter the number : "))
# mul=1
# while n!=0:
#     rem=n%10
#     mul*=rem
#     n=n//10

# print(f"Multiply of all digits of given number : {mul}")

"""WAPT ADD ALL THE DIGITS OF A GIVEN NUMBER ADD ONLY WHEN DIGIT MUST BE EVEN OTHERWISE SKIP. """

# n=int(input("Enter the number : "))
# sum=0

# while n!=0:
#     rem=n%10
#     if rem%2==0:
#         sum+=rem
#     n=n//10

# print(f"Sum of all digits of given number : {sum}")

"""WAPT REVERSE A GIVEN NUMBER USING WHILE LOOP."""
# n=int(input("Enter the number : "))
# rev=0
# while n!=0:
#     rem=n%10
#     rev=10*rev+rem
#     n//=10

# print(f"Reverse of a given number : {rev}")


"""WAPT CHECK WHETHER A GIVEN NUMBER IS PALINDROME OR NOT WHILE WHILE LOOP."""

# n=int(input("Enter the number : "))
# a=n
# rev=0
# while n!=0:
#     rem=n%10
#     rev=10*rev+rem
#     n//=10

# if a==rev:
#     print(f"The given number is Palindrome-- {a}")
# else:
#     print(f"The given number is not Palindrome --{a}")

"""WAPT CHECK WHETHER A GIVEN NUMBER IS ARMSTRONG NUMBER. """
# n=int(input("Enter the number : "))
# n2=n
# a=n2
# arm=0
# count=0
# while n!=0:
#     count+=1
#     n//=10
# print(f"The digit of given number is {count}")
# while n2!=0:
#     rem=n2%10
#     arm=arm+rem**count
#     n2//=10

# if a==arm:
#     print(f"The given number is armstrong number ")

# else:
#     print(f"The given number is not armstrong number")

