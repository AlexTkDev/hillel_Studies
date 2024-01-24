#                           ------------- EX 1 ----------
# Calculator

while True:
    num_1 = input('Enter a number 1: ')
    num_2 = input('Enter a number 2: ')
    action = input('Enter action, or break to exit the program: ')
    result = None

    if action == 'break':
        break

    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
    except:
        result = 'Invalid input entered'
    else:
        if action in ('+', '-', '/', '*'):
            match action:
                case '/':
                    if num_2 != 0:
                        result = num_1 / num_2
                    else:
                        result = 0
                case '+':
                    result = num_1 + num_2
                case '-':
                    result = num_1 - num_2
                case '*':
                    result = num_1 * num_2
        else:
            result = 'Invalid value, enter +, -, *, / '

    print(f'The result is = {result}')
