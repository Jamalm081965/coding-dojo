def say_hi(name):
    return "Hi " + name


greeting = say_hi("Michael")  # the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting)  # this will output 'Hi Michael'


def add(a, b):
    x = a + b
    return x


sum1 = add(4, 6)
sum2 = add(1, 4)
sum3 = sum1 + sum2
print(sum3)


# Challenge 1:
#   Fill in the missing code for the full_name function.
#   Be sure to add the 2 parameters (and name them appropriately)
#   Return the full name to get the desired output!

def full_name(first, last):
    return f"{first}  {last}"

name1 = full_name("Eddie", "Aikau")
print(name1) # should print Eddie Aikau


# Challenge 2:
#   Call the function again using your own name and print the results!
def full_name(first, last):
    return f"{first}  {last}"


name1 = full_name("Hussain", "Mohammad")
print(name1)
