# Basic Print all the integers from 0 to 150

# Space
space_1 = " 1 All the integers from 0 to 150"
print(space_1.center(50, "#"))
for i in range (0, 151):
    print(i)

# Space
space_2 = " 2 Multiples of fives "
print(space_2.center(50, "#"))

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range (5, 1001, 5):
    print(i)

# Space
space_3 = " 3 Counting, the Dojo Way "
print(space_3.center(50, "#"))

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range (1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")

# Space
space_4 = " 4 Whoa. That Sucker's Huge "
print(space_4.center(50, "#"))

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000 and print the final sum.
counter = 0
for i in range (0, 500000): # or I can use range (0, 500000, 2)
    if i % 2 != 0:          # if I use (0, 500000, 2) then i dont need this step
        counter += i
print(counter)

# Space
space_5 = " 5 Countdown by Fours "
print(space_5.center(50, "#"))


# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range (2018, 0, -4):
    print(i) 

# Space
space_6 = " 6 Flexible Counter "
print(space_6.center(50, "#"))

"""
Flexible Counter - Set three variables: low_num, high_num, mult. Starting at low_num and going through high_num, print only the integers that are a multiple of mult. For example, if low_num is 2, high_num is 9, and mult is 3, the loop should print 3, 6, 9 (on successive lines)
"""
low_num = 2
high_num = 10
mult = 3

for i in range (low_num, high_num, + 1):
    if i % mult == 0:
        print(i)