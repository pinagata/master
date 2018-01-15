l = [1,2,3,4,5]
for element in l:
    print(element)

for element in l:
    print('something!')

# modulo
print(10 % 3)
print(18 % 7)
print(4 % 2)
print('modulo in for loops')
# to check which numbers in a list are even
for num in l:
    if num % 2 == 0:
        print(num)
# to check which numbers are odd
for num in l:
    if num % 2 == 1:
        print(num)

for num in l:
    if num % 2 == 0:
        print('Here is an even')
    else:
        print('Odd number!')

for num in l:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number!')

list_sum = 0
for num in l:
    list_sum = list_sum + num
print(list_sum)
s = 'This is a string'
for letter in s:
    print(letter)
# for loops with a tuple
tup = (1,2,3,4,5)
for t in tup:
    print(t)

#tuple unpacking
l = [(2,4),(6,8),(10,12)]
print(l[0][0])
for tup in l:
    print(tup)
print('tuple unpacking')
for (t1,t2) in l:
    print(t1)
    print(t2)
    print(t1+t2)

# for loops with dictionaries
d = {'k1':1,'k2':2,'k3':3}
print(d)
for item in d:
    print item

# tuple unpacking for a dictionary
for (k,v) in d.iteritems():
    print(k)
    print(v)
# Python 3
for k,v in d.items():
    print(k)