#1
for i in range(1, 10, 1):
    print(i)

#Will print 1-10
#Wrong, prints 1-9 -- middle is i = 10; So doesn't run then. 

# #2
# for t in range(1, 10, 3):
#     print(t)

# #3
# for y in range(5):
#     if y < 5:
#         print(i)
#     elif y == 3:
#         print("i is 3")

# #4
# for j in range(20, 1, -3):
#     print(j)

# #5
# cities = ["London", "Paris", "Tokyo"]
# for city in cities:
#     print(city)

# #6
# numbers = [7, 13, 8, 42]
# for x in range(0, len(numbers)):
#     print(x)
#     print(numbers[x])
# if numbers[len(numbers) - 1] == 42:
#     print("The answer to life, the universe, and everything.")

# #7
# for num in range(10):
#     if num % 2 == 0:
#         print("Hello")
#     elif num % 4 == 0:
#         print("World")
#     else:
#         print(num)

# #8
# for num in range(10):
#     if num % 4 == 0:
#         print("Hello")
#     elif num % 2 == 0:
#         print("World")
#     else:
#         print(num)

# #9
# pet_info = {
#     "name": "Fido", 
#     "age": 4, 
#     "trick": "rolls over"
# }
# for key in pet_info:
#     print(key)
#     print(pet_info[key])

# #10
# things_to_remember = {
#     "First": "use the 20 minute rule and use the platform and other resources to find my answer",
#     "Second": "ask my classmates for help, like how I would ask a fellow employee at my job",
#     "Third": "ask an available TA in a public setting, so everyone can benefit from my question",
#     "Fourth": "ask an available instructor"
# }
# for num, step in things_to_remember.items():
#     print(num + ", I will " + step)
