
# numbers = [1, 2, 3, 1, 3, 4, 1, 4, 2, 5, 6, 7, 8, 9, 7, 4, 10]
# c = {}
# for i in numbers:
#     if i in c:
#         c[i] += 1
#     else:
#         c[i] = 1
# print(c)


# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#
#     return wrapper
#
#
# @do_twice
# def say_whee(a, b):
#     print(a + b)
#
#
# say_whee(2, 3)


# def add_s(func):
#     def wrapper(*args):
#         print("******")
#         func(*args)
#         print("******")
#     return wrapper
#
# @add_s
# def say_w(a,b):
#     print(a*b)
# say_w(3,5)

def add_s(func):
    def wrapper(*args):
        print("*******")
        try:
            func(*args)
        except ZeroDivisionError as d:
            print(f"sizda {d} xatolik")
        print("*******")
    return wrapper
@add_s
def s(d):
    print(42/d)

s(0)