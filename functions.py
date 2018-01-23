import math
def name_of_function(arg1, arg2):
    pass

print(name_of_function(1, 2))

def my_addition_func(arg1, arg2):
    """
    Here is my docstring
    """
    print(arg1 + arg2)
print(my_addition_func(1, 2))

def say_hello():
    print('hello')
print(say_hello())

def greeting(name):
    print('hello ' + name)
print(greeting('Jose'))

def add_num(num1,num2):
    return num1+num2
x = add_num(2,3)
print(x)
print(add_num('one','two'))

y = add_num('one','two')
print(y)

def is_prime(num):
    """
    This function checks for prime numbers
    or
    INPUT: A number
    OUTPUT: A print statement whether or not a number is prime
    or default pycharm
    """
    for n in range(2,num):
        if num % n == 0:
            print('Not Prime')
            break
    else:
        print('The number is prime')
print(is_prime(13))

def is_prime(num):
    """
    Better method for checking primes
    :param num:
    :return:
    """
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
        return True

print(is_prime(13))


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n) + 1)
    for divisor in range(3,sqr,2):
        if n % divisor == 0:
            return False
        return True
print(is_prime(24))