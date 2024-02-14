#                       ------------------  EX 1  ---------------------
from inspect import isgenerator


def prime_generator(end):
    # option 1
    # is_prime = (num for num in range(2, end + 1) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)))
    # return is_prime

    # # option 2
    def is_prime(x):
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    for num in range(2, end + 1):
        if is_prime(num):
            yield num


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')

