# 1.Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}
z = [{"x": 10, "y": 20}]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1] [0] = 15
print(x)


# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0]="Andres"
print(sports_directory)

# Change the value 20 in z to 30
z[0]["y"]= 30
print(z)


# 2.iterate Through a List of Dictionaries
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]
def iterate_dictionary(given_list):
    # Iterate through the list of dictionaries
    for student in given_list:
        # Format and print each dictionary as key-value pairs
        output = ", ".join(f"{key} - {value}" for key, value in student.items())
        print(output)


# Call the function
iterate_dictionary(students)

# 3.Get Values From a List of Dictionaries
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]

def iterate_dictionary2(first_name_key, given_list):
    for i in given_list:
        if first_name_key in i:
            print(i[first_name_key])
print("first name")
iterate_dictionary2("first_name", students)
print("last name")
iterate_dictionary2("last_name", students)

# Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
locatione_length = len(dojo["locations"])
print(locatione_length)

instructors_length = len(dojo["instructors"])
print(instructors_length)

print("")

location_heder = f"{locatione_length} Locations"
print(location_heder)


for place in dojo["locations"]:
    print(place)

print("")

instructors_header = f"{instructors_length} Instructors"
print(instructors_header)

for teacher in dojo["instructors"]:
    print(teacher)
