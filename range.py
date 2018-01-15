print(range(0,10))
print(range(11))
x = range(0,10)
print(x)
print(type(x))
start = 0
stop = 20
print(range(start,stop,3))

#python 2 has a built-in range generator called xrange() recommended for for loops
# range() outputs a list, xrange() will generate elements but not save them in memoruyu
l = [1,2,3,4,5]
for num in xrange(1,6):
    print(num)
x = xrange(1,6)
print(type(x))
# now it's a generator
x2 = range(1,6)
print(type(x2))
print(list(x))
print(x2 == list(x))
