# 1
# Biggie Size - 
# Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggieSize(list):
    for i in range(len(list)):
        if(list[i] > 0):
            list[i] = "big"
    return list

a = [-1, 3, 5, -5]
print(biggieSize(a))

# 2
# Count Positives - 
# Given a list of numbers, create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def countPositives(list):
    count = 0
    for i in range(len(list)):
        if(list[i] > 0):
            count += 1
    list[len(list) - 1] = count
    return list

c = [-1,1,1,1]
d = [1,6,-4,-2,-7,-2]

print(countPositives(c))
print(countPositives(d))

# 3
# Sum Total - 
# Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sumTotal(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

e = [1,2,3,4]
f = [6,3,-2]

print(sumTotal(e))
print(sumTotal(f))

# 4
# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def average(list):
    return sumTotal(list)/len(list)

avg = lambda list: sumTotal(list)/len(list)

print(f"Method says: {average(e)}")
print(f"Lambda says: {avg(e)}")

# 5
# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

length = lambda list: len(list)

g = [37,2,1,-9]
h = []

print(length(g))
print(length(h))

# 6
# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimun(list):
    if(len(list) == 0):
        return False
    min = 0
    for i in list:
        if(i < min):
            min = i
    return min

print(minimun(g))
print(minimun(h))

# 7
# Maximum - Create a function that takes a list and returns the maximum value in the array. 
# If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(list):
    if(len(list) == 0):
        return False
    max = 0
    for i in list: #when using for i in list --- notice that i = value of element, not index.
        if(i > max):
            max = i
    return max

print(maximum(g))
print(maximum(h))

# 8
# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the 
# sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimateAnalysis(list):
    analysis = {
        "sumTotal" : [], 
        "average" : [], 
        "minimum" : [],
        "maximum" : [],
        "length" : []
        }
    analysis["sumTotal"].append(sumTotal(list))
    analysis["average"].append(average(list))
    analysis["minimum"].append(minimun(list))
    analysis["maximum"].append(maximum(list))
    analysis["length"].append(len(list))
    return analysis

print(ultimateAnalysis(g))

# 9
# Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverseList(list):
    revver = 0
    for i in range (int(len(list) / 2)):
        revver = list[i]
        list[i] = list[len(list) - 1 - i]
        list[len(list) - 1 - i] = revver
    return list

print(reverseList(g))
