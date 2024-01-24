#                           ------------- EX 1 ----------
# modified Calculator

# while True:
#     num_1 = input('Enter a number 1: ')
#     num_2 = input('Enter a number 2: ')
#     action = input('Enter action, or break to exit the program: ')
#     result = None
#
#     if action == 'break':
#         break
#
#     try:
#         num_1 = float(num_1)
#         num_2 = float(num_2)
#     except:
#         result = 'Invalid input entered'
#     else:
#         if action in ('+', '-', '/', '*'):
#             match action:
#                 case '/':
#                     if num_2 != 0:
#                         result = num_1 / num_2
#                     else:
#                         result = 0
#                 case '+':
#                     result = num_1 + num_2
#                 case '-':
#                     result = num_1 - num_2
#                 case '*':
#                     result = num_1 * num_2
#         else:
#             result = 'Invalid value, enter +, -, *, / '
#
#     print(f'The result is = {result}')


#                           ------------- EX 2 ----------
from keyword import kwlist

result = True

value_name = "_"
# value_name = "x"
# value_name = "get_value"
# value_name = "get value"
# value_name = "get!value"
# value_name = "some_super_puper_value"
# value_name = "Get_value"
# value_name = "get_Value"
# value_name = "getValue"
# value_name = "3m"
# value_name = "m3"

literal = '''!"#$%&'()*+,-./:;<=>?@[]{}\\^`|~'''
kw_list = kwlist

if not value_name[0].isdigit() and not value_name[0].isupper():
    if not value_name.isdigit() and not value_name.isupper():
        if value_name.find(" ") == -1:
            if value_name not in kw_list:
                for letter in value_name:
                    if letter not in literal and not letter.isupper():
                        result = True

                    else:
                        result = False
                        break
        else:
            result = False
else:
    result = False

print(result)
