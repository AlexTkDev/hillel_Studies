#                   ------------------- EX 1 --------------------

users = [{"name": "John", "age": 15},
         {"name": "Jack", "age": 45},
         {"name": "Alex", "age": 35},
         {"name": "Nicolas", "age": 15},
         {"name": "Ann", "age": 25},
         {"name": "Tod", "age": 24},
         {"name": "Tonni", "age": 18},
         ]

min_age = min(age["age"] for age in users)
jr_names = [name["name"] for name in users if name["age"] == min_age]

max_long_name = max(len(name["name"]) for name in users)
longest_name = [name["name"] for name in users if len(name["name"]) == max_long_name]

md_age = sum(age["age"] for age in users) / len(users)
middle_age = round(md_age, 2)

print(f"The names is young people {jr_names}\n"
      f"The max length name is {middle_age}\n"
      f"The middle age is {middle_age}"
      )
