#1
#Update Values in Dictionaries and Lists

    #A Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
    #B Change the last_name of the first student from 'Jordan' to 'Bryant'
    #C In the sports_directory, change 'Messi' to 'Andres'
    #D Change the value 20 in z to 30

x = [ 
    [5,2,3], 
    [10,8,9] 
    ] 

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
    }

z = [ 
    {'x': 10, 'y': 20} 
    ]

def changeAllMethods():
    #A Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
    for arr in x:
        if (arr[0] == 10):
            arr[0] = 15
    #B Change the last_name of the first student from 'Jordan' to 'Bryant'
    students[0]['last_name'] = 'Bryant'
    #C In the sports_directory, change 'Messi' to 'Andres'
    sports_directory['soccer'][0] = 'Andres'
    #D Change the value 20 in z to 30
    z[0]['y'] = 30
    print(x)
    print(students)
    print(sports_directory)
    print(z)

# changeAllMethods()

#2
#Iterate through a list of dictionaries
# Create a function iterateDictionary(some_list) that, 
# given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. 
# For example, given the following list:

def iterateDictionary(list):
    for student in students:
        print("first_name - " + student['first_name'] + ", last_name - " + student['last_name'])

# iterateDictionary(students)

#3
# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, 
# given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:

def iterateDictionary2(key, list):
    for each in list:
        print(each[key])

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

#4
# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that 
# given a dictionary whose values are all lists, prints the name of each key along with the size of its list, 
# and then prints the associated values within each key's list. 

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
    }

def printInfo(dict):
    for each in dict:
        print(len(dict[each]), str(each).upper())
        for x in dict[each]:
            print(x)
        print(" ")

printInfo(dojo)
