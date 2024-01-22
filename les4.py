#               ---------------- EX 1 -----------------
#
# my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
#
# temp_list = [i for i in my_list if i == 0]
# my_list = [i for i in my_list if i != 0] + temp_list
# print(my_list)

#           option two
#
# my_list = [1, 0, 13, 0, 0, 0, 5, 9, 9, 9, 9, 0, 0, 0, 0, 6, 7, 5, 4, 3, 6, 7, 5, 4, 3, 0, 6, 7, 5,
#            4, 3, 6, 7, 5, 4, 3]
#
# my_list.sort(key=bool, reverse=True)
# print(my_list)


#               ---------------- EX 2 -----------------
#
my_list = [0, 1, 7, 2, 4, 8]
res = 0

if len(my_list) == 0:
    res = 0
else:
    for i in my_list[::2]:
        res += i
    res *= my_list[-1]

print(res)
