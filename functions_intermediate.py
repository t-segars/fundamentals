# 1

# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# def change(x):
#     for i in range(0, len(x)):
#         x[1] = [15,8,9]
#     return x
# y = change(x)
# print(y)

# def change1(students):
#     for i in range(0, len(students)):
#         students[0]= {'first_name': 'Jordan', 'last_name': 'Bryant'}
#     return students
# y = change1(students)
# print(y)

# def change2(sports_directory):
#     for i in range(0, len(sports_directory)):
#             sports_directory = {'soccer' : ['Andres', 'Ronaldo', 'Rooney']}
#     return sports_directory
# y = change2(sports_directory)
# print(y)


# 2

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(some_list):
#     for curr_dict in some_list:
#         display_str = ""
#         for curr_key in curr_dict.keys():
#             display_str += f"{curr_key} - {curr_dict[curr_key]}, "
#         display_str = display_str[:len(display_str) - 2]
#         print(display_str)
# iterateDictionary(students)

# 3



# def iterateDictionary2(key_name, some_list):
#     for curr_dict in some_list:
#         print (curr_dict[key_name])

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

# 4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict.keys():
        print(f'{len(some_dict[key])} {key.upper()}')
        for item in some_dict[key]:
            print(item)
        print('\n')
printInfo(dojo)