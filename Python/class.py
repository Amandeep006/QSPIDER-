
# We see the use of documentation string in the class
# class sample():
#     """This is the sample class for  the demo purpose."""
#     # Variable
#     # methods 

# class demo():
#     """This is the demo class for the demo purpose."""
#     # Variable 
#     # methods 

# # className.__doc__ is the syntax for the print the documentation string and all documnetation string store automatically in the __doc__.
# print(sample.__doc__)
# print(sample.__doc__)


"""
WAPT PRINT STUDENT NAME AND HIS ROLL NUMBER USING CLASS.
"""
class Student():
    def __init__(self, name , roll):
        self.name=name
        self.roll=roll

    def display(self):
        print(f"My name is {self.name}")
        print(f"My roll is {self.roll}")

s1=Student("Palak",58)
s1.display()
print(s1.name,s1.roll)