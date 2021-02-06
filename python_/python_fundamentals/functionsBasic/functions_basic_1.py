# #1
# def a():
#     return 5
# print(a())
# #5

# #2
# def a():
#     return 5
# print(a()+a())
# #10

# #3
# def a():
#     return 5
#     return 10
# print(a())
# #5

# #4
# def a():
#     return 5
#     print(10)
# print(a())
# #5

# #5
# def a():
#     print(5)
# x = a()
# print(x)
# #5, None (because although it prints, it returns no value. 5 will also not be printed until x is printed and a() is run)

# #6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))
#3, 5, Error (cannot print a() + a() because there is nothing being returned from the func. In which case, although nums are printed when func runs, nothing is returned, so there is nothing to add when print tried to add a() and a())

# #7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))
# #25

# #8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())
# #100, 7
# #returns 10 not 7 --- because the if will never be true, so else always runs. Thus always returns 10

# #9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))
# #7, 14, 7, 14, error
# #I was wrong, we are no longer printing. 7, 14, yes. But last one returns values, so adds 7 and 14 = 21

# #10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))
# #8

# #11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)
# #500, 500, 300, 500

# #12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)
# #500, 500, 300, 500

# #13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)
# #500, 500, 300, 300

# #14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()
# #1, 3, 2

# #15
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)
# #1, 3, 5, 10
