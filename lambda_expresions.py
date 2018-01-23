def square(num):
    result = num**2
    return result
print(square(4))

def square(num):
    return num**2
print(square(5))

def square(num): return num**2
print(square(7))

square = lambda num: num**2
print(square(10))

#check if a number is even
even = lambda num: num % 2 == 0
print(even(7))

def even(num):
    return num % 2 == 0
print(even(5))

# grabs the first letter of a string
first = lambda s: s[0]
print(first('hello'))

# reverse the string
rev = lambda s: s[::-1]
print(rev('hello'))

def adder(x,y):
    return x+y
print(adder(2,3))

adder = lambda x,y: x+y
print(adder(4,6))