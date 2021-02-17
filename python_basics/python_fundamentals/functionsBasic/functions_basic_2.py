#1
# Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

#create empty array
#for loop; set i = num; i--
#push i into array
#return array

def countdown(num):
    newList = []
    for i in range(num, -1 , -1):
        newList.append(i);
    return newList

test1 = countdown(5)
print(test1)

#2
# Print and Return - Create a function that will receive a list with two numbers. 
# Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def printAndReturn(list):
    if(len(list) < 2):
        return "List must contain 2 elements at least."
    print(list[0])
    return list[1]

test2 = printAndReturn([1,2])
print(f"My returned value is: {test2}")

#3
# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def firstPlusLength (list):
    return list[0] + len(list)

firstPlusLen = lambda list: list[0] + len(list)

testList1 = [1,2,3,4,5]
print(f"Lambda says: {firstPlusLen(testList1)}")
print(f"Method says: {firstPlusLength(testList1)}")

#4
# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original 
# list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def valuesGreaterThanSecond(list):
    if(len(list) < 2):
        return False
    newList = []
    for i in range(len(list)):
        if(list[i] > list[1]):
            newList.append(list[i])
    print(len(newList))
    return newList

a = valuesGreaterThanSecond([5,2,3,2,1,4])
b = valuesGreaterThanSecond([3])

print(a)
print(b)

#5
# This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def thisLengthThatValue(size, val):
    newList = []
    for i in range(size): #if the size is 4 --- since stop is EXCLUSIVE --- i = 4 works. 'cause list is 0-index so 0-3 is 4.
        newList.append(val)
    return newList

c = thisLengthThatValue(4,7)
d = thisLengthThatValue(6,2)

print(c)
print(d)
