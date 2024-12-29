#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

output:
5 


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

output:
NameError: name 'number_of_days_in_a_week_silicon_or_triangle_sides' is not defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

output:
5  #any thing after the return statement gets ignored

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

output:
5  #any thing after the return statement gets ignored

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

output:
5
none 
#function without return statement always return "none"

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
output:
TypeError: NoneType 

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

outout:
25
# integers are converted to string with return str(b)+str(c)

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

output:
100
10
# 3rd return statement wont print because else block is true. 


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

output:
7
14
21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

output:
8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

output:
500
500
300
500
# b in the foobar will not affect the global variable b which out side the function


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

output:
500
500
300
500 
# return is not used 


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

output:
500
500
300
300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

output:
1
3
2
# I look some help from google to understand and look at some examples 

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

output:
1
3
5
10
"""
Step-by-Step Execution:
Function Definitions:

foo() and bar() are defined.
foo() calls bar() within its execution.
Function Call (y = foo()):

foo() is called, and its return value will be stored in y.
Execution of foo():

Step 1: print(1) → Outputs 1.
Step 2: x = bar() → Calls bar():
Execution jumps to bar().
Step 2.1: print(3) in bar() → Outputs 3.
Step 2.2: return 5 → Returns 5 to foo().
Step 3: print(x) → Prints the value of x (which is 5).
Step 4: return 10 → Returns 10 to the caller (assigns it to y).
Print y:

print(y) prints the value of y, which is 10.

Explanation:
The foo() function calls bar(), captures its return value (5) in x, and then prints it.
foo() itself returns 10, which is assigned to y and printed.
"""