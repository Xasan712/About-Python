# menu = """
# 1.Accept Student
# 2.All    Student 
# 3.Search Student
# 4.Delete Student
# 5.Update Student 
# 6.Exit
# """
# users = []
# while True:
#     x = input(menu)
#     if int(x) == 1:
#         user = input("student name: ")
#         users.append(user)
#         print(f"add student: {user}")

#     elif int(x) == 2:
#         print(users)
#     elif int(x) == 3:
#         finduser = str(input("Name surname: "))
#         if finduser in users:
#             print(f"{finduser} ro`yxatda bor")
#     elif int(x) == 4:
#         deleteuser = str(input("Name surname: "))
#         users.remove(deleteuser) 
#         print("succesfully deleted")      
#     elif int(x) == 5:
#         update = input("Kimni update qilmoqchisiz")
#         if update in users:
#             update2 = input("yangi ism kiriting:")
#             users.append(update2)
#             users.remove(update)
#             print("Foydalanuvchi o'zgartirildi!")
#     elif int(x) == 6:    
#         print("Dastur to`xtatildi")   
#         break 


# a = [   1, 2, 3, 4, 5, 6, 7,
#     3, 4, 5, 6, 7, 8, 9,
#     12, 34, 45, 56, 57,
#     31, 21, 43, 13, 45
# ]
# d = []
# for i in a:
#     if i%5==0:
#         d.append(i)
# print(d)        

# a = [
#     [1, 2, 3, 4, 5, 6, 7],
#     [3, 4, 5, 6, 7, 8, 9],
#     [12, 34, 45, 56, 57],
#     [31, 21, 43, 13, 45]
# ]
# d = []
# for i in a:
#     for x in i:
#         if x % 5 == 0:
#             d.append(x)

# print(d)


