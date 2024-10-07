from pprint import pprint
# a = {
#     'name':'Xasan',
#     'surname' : 'Xoliqnazarov',
#     'interests' : 'Social Networking and Freelance',
#     'color' : 'dark green and dark blue', 
#     'age': 16,
# }
# print(a)

#Hometask -1
# task - 1
# subjects = {
#     'Python' : 5,
#     'Matematika' : 5,
#     'Ingiliz t' : 5,
# } 
# a = subjects['Ingiliz t']=4
# print(subjects)

# task - 2
# subjects = {
#     'Python' : 5,
#     'Matematika' : 5,
#     'Ingiliz t' : 5,
# } 
# subjects.setdefault('Tarix', 5)
# print(subjects)

# task - 3

# subjects = {
#     'Python' : 5,
#     'Matematika' : 5,
#     'Ingiliz t' : 5,
# } 
# subjects.setdefault('Tarix', 5)
# print(subjects)

# task - 4

# dictionary = {
#     "hello": "salom",
#     "book": "kitob",
#     "water": "suv",
#     "food": "ovqat",
#     "house": "uy",
#     "car": "mashina",
#     "sun": "quyosh",
#     "friend": "do'st",
#     "school": "maktab",
#     "city": "shahar"
# }
# print(dictionary)

# dictionary2 = {
#     "tree": "daraxt",
#     "sky": "osmon",
#     "cat": "mushuk",
#     "dog": "it",
#     "flower": "gul",
#     "river": "daryo",
#     "mountain": "tog'",
#     "milk": "sut",
#     "door": "eshik",
#     "phone": "telefon"
# }
# print(dictionary2)


#Hometask - 2

# task -1

# movie = {
#     'Nomi':    'To`lqin zarbasi',
#     'Janr':    'Jangari/Fantastika',
#     'Davlati': 'Aqsh',
#     'Tili':    'Uzbek tilida',
# }
# pprint(movie)


# task - 2

# movie = {
#     'Nomi':    'To`lqin zarbasi',
#     'Janr':    'Jangari/Fantastika',
#     'Davlati': 'Aqsh',
#     'Tili':    'Uzbek tilida',
# }
# pprint(movie.get('Janr'))

# task - 3

# movie = {
#     'Nomi':    'To`lqin zarbasi',
#     'Janr':    'Jangari/Fantastika',
#     'Davlati': 'Aqsh',
#     'Tili':    'Uzbek tilida',
# }
# movie.setdefault('Tili','Ingiliz tili')                                           ??????????
# pprint(movie)



# task - 4
# movie = {
#     'Nomi':    'To`lqin zarbasi',
#     'Janr':    'Jangari/Fantastika',
#     'Davlati': 'Aqsh',
#     'Tili':    'Uzbek tilida',
# }

# m_copy = movie.copy()
# pprint(m_copy)

# task - 5
# a)
        # movie = {
        #     'Nomi':    'To`lqin zarbasi',
        #     'Janr':    'Jangari/Fantastika',
        #     'Davlati': 'Aqsh',
        #     'Tili':    'Uzbek tilida',
        # }
        # movie.pop('Tili')                    # pop ga liritilgan key ochirildi value bilan    
        # print(movie)
# b)
# movie = {
#     'Nomi':    'To`lqin zarbasi',
#     'Janr':    'Jangari/Fantastika',
#     'Davlati': 'Aqsh',
#     'Tili':    'Uzbek tilida',
# }
# movie.popitem()                                 # oxiridagi o`chdi`
# print(movie) 

# task - 6

# movie = {
#     'Nomi':    'To`lqin zarbasi',
#     'Janr':    'Jangari/Fantastika',
#     'Davlati': 'Aqsh',                                              # None
#     'Tili':    'Uzbek tilida',
# }
# pprint(movie.clear())


# task - 7
# movie = {
#     'Nomi':    'To`lqin zarbasi',
#     'Janr':    'Jangari/Fantastika',
#     'Davlati': 'Aqsh',
#     'Tili':    'Uzbek tilida',
# }
# pprint(movie)
# pprint('------------------------')
# m_copy = movie.copy()
# pprint(m_copy)



