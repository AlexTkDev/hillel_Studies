# #                   ------------------- EX 1 --------------------
#
# users = [{"name": "John", "age": 15},
#          {"name": "Jack", "age": 45},
#          {"name": "Alex", "age": 35},
#          {"name": "Nicolas", "age": 15},
#          {"name": "Ann", "age": 25},
#          {"name": "Tod", "age": 24},
#          {"name": "Tonni", "age": 18},
#          ]
#
# min_age = min(age["age"] for age in users)
# jr_names = [name["name"] for name in users if name["age"] == min_age]
#
# max_long_name = max(len(name["name"]) for name in users)
# longest_name = [name["name"] for name in users if len(name["name"]) == max_long_name]
#
# md_age = sum(age["age"] for age in users) / len(users)
# middle_age = round(md_age, 2)
#
# print(f"The names is young people {jr_names}\n"
#       f"The max length name is {middle_age}\n"
#       f"The middle age is {middle_age}"
#       )


#                   ------------------- EX 2 --------------------

my_dict_1 = {1: 1, 22: 2, 3: 3, 4: 4, 5: 5, 67: 6}
my_dict_2 = {1: 1, 9: 2, 3: 10, 4: 4, 5: 8, 6: 7}

in_two_dict = [key for key in my_dict_1.keys() if key in my_dict_2]

only_first_keys = [key for key in my_dict_1.keys() if key not in my_dict_2]

only_in_the_first = {key: my_dict_1[key] for key in my_dict_1.keys() if key not in my_dict_2}

merged_dict = {}
for key, value_1 in my_dict_1.items():
    if key in my_dict_2:
        merged_dict[key] = [value_1, my_dict_2[key]]
    else:
        merged_dict[key] = value_1

for key, value_2 in my_dict_2.items():
    if key not in my_dict_1:
        merged_dict[key] = value_2

print(f"a) Список із ключів, які є в обох словниках: {in_two_dict}\n"
      f"б) Список із ключів, які є у першому, але немає у другому словнику: {only_first_keys}\n" 
      f"в) Значення для ключів, які є в першому, але немає в другому словнику: {only_in_the_first}\n"
      f"г) Об'єднання двох словників: {merged_dict}"
      )
