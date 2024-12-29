# CountDown
def count_down(start):
    new_list = []
    for i in range (start, -1, -1):
        new_list.append(i)
    return new_list
result = count_down(5)
print(result)

# Print and Return
def print_return(num1, num2):
    
        print(num1)
        return num2
result = print_return(1,2)
print(result)

# First plus length ( I look some help from chat GPT)
def first_plus_length(number_list):
    return number_list[0] + len(number_list)
given_list = [2, 4, 6, 8]
results = first_plus_length(given_list)
print(results)

# Values Greater than Second
def values_greater_than_second(num_list):
    if len(num_list) < 2:
        return False
    second_value = num_list[1]
    new_list = []
    for i in num_list:
        if i > second_value:
            new_list.append(i)
    print(len(new_list))
    return new_list

given_list = [1, 2, 3, 4, 5, 6]
print(values_greater_than_second(given_list))


# This Length, That Value
def this_length_that_value(length, size):
    length_and_value = []
    for i in range(length):
        length_and_value.append(size)
    return length_and_value 
print(this_length_that_value(3, 9))
print(this_length_that_value(6, 8))

"""
Explanation of Fixes:
Changed length to Range Iteration:

Instead of iterating over length (which is not iterable), we use for _ in range(length) to loop the correct number of times.
Moved length_and_value Initialization:

length_and_value is initialized outside the loop to ensure it persists and accumulates values.
Fixed return Placement:

The return statement is moved outside the loop, so the function only returns after the list is fully constructed.
Avoided Returning append:

The append method is called to add items to the list, but the function now returns the list directly after all operations.
"""
