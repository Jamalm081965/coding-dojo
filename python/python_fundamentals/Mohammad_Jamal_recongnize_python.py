num1 = 42 #Var declear for intger type is numerical 
num2 = 2.3 #var delear for float type numerical 
boolean = True # this is var the type is boolean (true or fales)
string = "Hello World" #string 
pizza_toppings = ["Pepperoni", "Sausage", "Jalepenos", "Cheese", "Olives"] # this list 
person = {"name": "John", "location": "Salt Lake", "age": 37, "is_balding": False} #dictionary 
fruit = ("blueberry", "strawberry", "banana")
print(type(fruit)) # this tuples 
print(pizza_toppings[1]) # print statement it prints the sausage because index value for 1 
pizza_toppings.append("Mushrooms") #this add the mushroom in the list 
print(person["name"]) # This prints john from dictionary 
person["name"] = "George" # add george to name key 
person["eye_color"] = "blue"  # add blue to eye_color key
print(fruit[2]) # this will print the banana from tuple call fruit

if num1 > 45:    # setting up the condition 
    print("It's greater") # print statement if "if" condition is met
else: # setting else statement if the "if condition is not met this do else"
    print("It's lower") #print else statement 

if len(string) < 5: #setting the the condition using string lenght 
    print("It's a short word!") #print statement if the condition is met 
elif len(string) > 15: #elif condition if the "if" condition is not met
    print("It's a long word!") #print statement for elif statement 
else: #setting else if the "if" or "elif" condition is met then I will else condition 
    print("Just right!") #print else statement 


    """
    Below this for and while loops and their print statement. 
    it print the var "x'
    """

for x in range(5): 
    print(x)
for x in range(2, 5):
    print(x)
for x in range(2, 10, 3): # this for loop will incriment by 3
    print(x)
x = 0
while x < 5:
    print(x)
    x += 1 # this one will add 1 to the value x until x is less than 5 and start at 0


pizza_toppings.pop() # this is one remove the last index value from the list 
pizza_toppings.pop(1)  # this is one remove the index value from the index 1

print(person) # this dictionary defind above 
person.pop("eye_color")  # this will remove the key value called eye_color 
print(person) # this dictionary defind above after removing the eye_color 

"""
this for loop 
"""
for topping in pizza_toppings:
    if topping == "Pepperoni":
        continue
    print("After 1st if statement")
    if topping == "Olives":
        break

"""
this function to print 
Hello with for loop 
"""
def print_hello_ten_times():
    for num in range(10):
        print("Hello")


print_hello_ten_times()

"""
this function to print 
"""

def print_hello_x_times(x):
    for num in range(x):
        print("Hello")


print_hello_x_times(4)



def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print("Hello")


print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
