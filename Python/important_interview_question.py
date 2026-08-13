"""IMPORTANT INTERVIEW QUESTIONS """


"""
WAPT SOLVE THE GIVEN BELOW REQUIREMENT.
INPUT--> WE ARE LEARNING PYTHON AND IT IS EASY TO LEARN.
OUTPUT--> LEARN TO EASY IS IT AND PYTHON LEARNING ARE WE.
"""

# s=input("Enter your sting : ")
# l=s.split()
# value=l[::-1]
# # USE JOIN TO  {  " ".JOIN(VALUE)      }     
# out=(" ".join(value))
# print(out)


"""
WAPT SOLVE THE GIVEN BELOW REQUIREMENT.
INPUT-->  WE LOVE TO CODE  IN PYTHON.
OUTPUT-->  WE EVOL TO EDOC IN NOHTYP.
"""

"""use of for loop"""
# s=input("Enter the string : ")
# l=s.split()
# for i in range(0,len(l)-1):
#     if i%2!=0:
#         l[i]=l[i][::-1]

# out=(" ".join(l))
# print(out)

""" while loop """
# s=input("Enter the string : ")
# l=s.split()
# a=[]
# i=0
# while i<len(l):
#     if i%2==0:
#         a.append(l[i])
#     else:
#         l[i]=l[i][::-1]
#         a.append(l[i])

#     i+=1

# out=(" ".join(l))
# print(out)


"""WAPT SOLVE THE GIVEN BELOW REQUIREMENT. 
INPUT--> WE LOVE TO CODE IN PYTHON 
OUTPUT--> NOHTYP NI EDOC OT EVOL EW.
"""

""" Using only string concept """
# s=input("Enter the string : ")
# print(s[::-1])

"""Using while loop"""
# s=input("Enter the string : ")
# l=s.split()
# l1=l[::-1]
# res=[]
# for i in l1:
#     res.append(i[::-1])

# out=" ".join(res)
# print(out)


"""WRPT SOLVE THE GIVEN BELOW REQUIREMENT 
INPUT---> A4B3C3
OUPTUT--> AAAABBBCCC
"""

# repelication opertor : "Hello"*4---> "HelloHelloHelloHello"
# s=input("Enter the input: ")
# out=""
# for i in s:
#     if i.isalpha():
#         x=i
#     else:
#         d=int(i)
#         out=out+x*d

# print(out)

"""
WRPT SOLVE THE GIVEN BELOW REQUIREMENT 
INPUT---> B3C2A4
OUTPUT-->AAAABBBCC
"""
#sorted()- it is build-in function which is used to sort the datatype but in the list form.
# s=input("Enter the input: ")
# out=""
# for i in s:
#     if i.isalpha():
#         x=i
#     else:
#         d=int(i)
#         out=out+x*d
# v=sorted(out)
# res="".join(v)
# print(res)

"""
WAPT COUNT THE OCCURANCE OF EACH AND EVERY CHARCTER PRESENT INSIDE THE GIVEN STRING.
INPUT--> ABABCA
OUTPUT--> {"A":3,"B":2,"C":1}
"""

# s=input("Enter the string :")
# d={}
# for i in s:
#     d[i]=d.get(i,0)+1

# print(d)

"""
WAPT COUNT THE OCCURANCE OF EACH AND EVERY CHARCTER PRESENT INSIDE THE GIVEN STRING.
INPUT--> ABABCA
OUTPUT--> A OCCURED 3 TIMES 
          B OCCURED 2 TIMES 
          C OCCURED 1 TIMES 
"""
# s=input("Enter the string :")
# d={}
# for i in s:
#     d[i]=d.get(i,0)+1

# for i in d:
#     print(f"{i} occured {d.get(i)} times")

"""
WAPT SOLVE THE BELOW GIVEN REQUIREMENT
INPUT--> ABABCA
OUTPUT-->3A2B1C
"""
# s=input("Enter the string :")
# d={}
# for i in s:
#     d[i]=d.get(i,0)+1
# out=""
# for i in d:
#     # print(f"{d[i]}{i}",end="")
#     """convert it into string """
#     out=out+str(d[i])+i

# print(out)

"""WAPT TAKE A STRING AS INPUT, ASSUME INPUT STRING CONTAINS ONLY ALPHABET AND DIGITS, WRITE A CODE TO SORT CHARACTERS OF A STRING FIRST APHABET SYMBOL FOLLOWED BY DIGIT.
INPUT---> D5A2B1
OUPTPUT--> ABD125
"""

s=input("Enter the string : ")
a="" 
d=""
for i in s:
    if i.isalpha():
        a+=i

    else: 
        d+=i

out=sorted(a)+sorted(d)
res="".join(out)
print(res)