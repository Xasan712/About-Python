# def count_down(start):
#     print(start)
#     x = start -1
#     if x > 0:
#         count_down(start-1)
#
# count_down(7)

# def fn(n):
#     s = 1
#     for i in range(1,n+1):
#         s *= i
#     return s
# print(fn(5))

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
# print(fact(3))

# def facts(n):
#     if n <= 0:
#         return "Error"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return facts(n - 1) + facts(n - 2)
# n = 13
# print(f"{n} = {facts(n)}")


def fib(n):
    if n==0:
        return 0
    elif n == 1  or n ==2:
            return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(7))


# Python Recursive Function

# def func():
#     ...
#     func()

# def fn():
#     # ...
#     if condition:
#         # stop calling itself
#     else:
#         fn()
#     # ...

# def count_down(start):
#     """ Count down from a number """
#     print(start)
#     x = start - 1
#     if x > 0:
#         count_down(start - 1)
#
#
# count_down(7)

# def calls(n):
#     data = 0
#     for x in range(n + 1):
#         data += x  # data = data + x
#     return data
#
#
# print(calls(10))
#
# Factorial
# factorial(3)          # 1st call with 3
# 3 * factorial(2)      # 2nd call with 2
# 3 * 2 * factorial(1)  # 3rd call with 1
# 3 * 2 * 1             # return from 3rd call as number=1
# 3 * 2                 # return from 2nd call
# 6                     # return from 1st call


# def fn(n):
#     s = 1
#     for x in range(1, n + 1):
#         s *= x
#     return s
#
#
# print(fn(3))

# fact(3) : 1 * 2 * 3 = 6 Recursive Function
