#1
for i in range(1, 10, 1):
    print(i)

# Will print 1-10
# Wrong, prints 1-9 -- middle is i = 10; So doesn't run then. 

#2
for t in range(1, 10, 3):
    print(t)

#prints 1 4 7

#3
for y in range(5):
    if y < 5:
        print(i)
    elif y == 3:
        print("i is 3")

#prints 1 2 "i is 3" 4
#har har -- we are using var y. i is undefined and so throws error that i is underfined. 

#4
for j in range(20, 1, -3):
    print(j)

#prints 20 17 14 11 8 5 2

#5
cities = ["London", "Paris", "Tokyo"]
for city in cities:
    print(city)

#prints London, Paris, Tokyo

#6
numbers = [7, 13, 8, 42]
for x in range(0, len(numbers)):
    print(x)
    print(numbers[x])
if numbers[len(numbers) - 1] == 42:
    print("The answer to life, the universe, and everything.")

#Prints 0 7,  1 13, 2 8, 3 42 Witty reference ;)

#7
for num in range(10):
    if num % 2 == 0:
        print("Hello")
    elif num % 4 == 0:
        print("World")
    else:
        print(num)

#prints 1 "hello" 3 "hello" 5 "hello" 7 "hello" 9 
#missed the "hello" from num = 0;

#8
for num in range(10):
    if num % 4 == 0:
        print("Hello")
    elif num % 2 == 0:
        print("World")
    else:
        print(num)

#prints "Hello" 1 "World" 3 "Hello" 5 "World" 7 "Hello" 9 

#9
pet_info = {
    "name": "Fido", 
    "age": 4, 
    "trick": "rolls over"
}
for key in pet_info:
    print(key)
    print(pet_info[key])

#prints name fido, age 4, trick rolls over

#10
things_to_remember = {
    "First": "use the 20 minute rule and use the platform and other resources to find my answer",
    "Second": "ask my classmates for help, like how I would ask a fellow employee at my job",
    "Third": "ask an available TA in a public setting, so everyone can benefit from my question",
    "Fourth": "ask an available instructor"
}
for num, step in things_to_remember.items():
    print(num + ", I will " + step)

#prints First, I will use the 20... Second, I will ask my class.... Third, I will ask an available.... Fourth, I will ask an available...
