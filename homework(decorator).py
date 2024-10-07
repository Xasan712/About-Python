# def decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# def say_whee():
#     print("Whee!")
#
# say_whee = decorator(say_whee)

# _______________________---
# from decorators import do_twice
#
# @do_twice
# def greet(name):
#     print(f"Hello {name}")

# >>> greet(name="World")
# Traceback (most recent call last):
#   ...
# TypeError: wrapper_do_twice() takes 0 positional arguments but 1 was given
#
# problem= ''''
# Muammo shundaki, ichki funktsiya wrapper_do_twice()hech qanday argumentlarni qabul qilmaydi,
# lekin siz name="World"unga o'tdingiz. Buni bitta argumentni qabul qilishga ruxsat berish orqali
# tuzatishingiz mumkin , lekin keyin bu siz avval yaratgan funksiya wrapper_do_twice()uchun ishlamaydi .say_whee()
# '''