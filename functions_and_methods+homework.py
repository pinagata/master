# the volume of a sphere when radius given
from __future__ import division



def vol(rad):
    pi = 22/7
    return (4 / 3) * pi * (rad ** 3)


print(vol(5))

# one more way


def vol(rad):
    pi = 22/7
    volume = (4/3) * (pi * rad**3)
    return volume


print(vol(5))

# the formula itself
print((4/3) * (22/7) * 5**3)

# checks whether a number is in a given range (inclusive of high and low)


def ran_check(num, low, high):
    for num in range(low, high+1):
        if low >= num <= high:
            return 'In range'
        else:
            return 'Not in range'


print(ran_check(4, 5, 90))

# his solution


def ran_check(num,low,high):
    if num in range(low,high+1):
        print ("%s is in the range" %str(num))
    else:
        print('The number is outside the range.')


# if I wanted to return boolean
def ran_bool(num,low,high):
    for num in range(low,high+1):
        if low >= num <= high:
            return True
        else:
            return False


print(ran_bool(3,3,8))

# shorter version


def ran_bool(num,low,high):
    return num in range(low,high+1)


print(ran_bool(5,1,5))

# function that accepts a string + calculating the number of upper and lower case letters


d = {'upper': 0, 'lower': 0}


def up_low(s):
    for c in s:
        if c.isupper():
            d['upper'] += 1
        elif c.islower():
            d['lower'] += 1
        else:
            pass


s = 'Hello Darkness My Old Friend'
print('Original string: ', s)
print('No. of upper case characters: ', d['upper'])
print('No. of lower case characters: ', d['lower'])
print(up_low(s))


# write a list that returns a new list with unique values


def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x


print(unique_list([1,1,1,1,2,2,2,3,3,4,5]))


# a function tha mulitplies all numbers in a list

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


print(multiply([8, 2, 3, -1, 7]))


def palindrome(s):
    s = s.replace(' ', '')
    return s == s[::-1]


print (palindrome('madam'))

# a function that checks if a string is a pangram or not
import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())


ispangram('The quick brown fox jumps over the lazy frog')
print(string.ascii_lowercase)