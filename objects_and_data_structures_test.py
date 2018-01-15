# Numbers
print (2000 - (25 * 4 / 2) + (5 ** 2 + 25.25) - 1900)
print (2 / 3)
print(2.0 / 3)
print(2 // 3)
print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5)

print(4 ** 0.5)
print(4 ** 2)

# Strings
s = 'hello'
print(s[1])
print(s[::-1])
print(s[4])
print(s[-1])
print(s[-1:])

# Lists
l_1 = [0,0,0]
print(l_1)
# one more way of creating lists?
l_2 = [0,0]
print(l_2.append(0))
print(l_2)
l_3 = [0]
print(l_3*3)
l = [1,2,[3,4,'hello']]
print(l)
print(l[2][2])
l[2][2] = 'goodbye'
print(l)

l = [5,3,4,6,1]
l.sort()
print(l)

# Dictionaries
d = {'simple_key':'hello'}
print(d['simple_key'])
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1])
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d)
print(d['k1'][2]['k2'][1]['tough'][2])

# Tuples
t = (1,2,3, 4,1)
print(t)
print(t.count(1))
print(t.index(3))

# Sets
l = [1,2,2,33,4,4,11,22,3,3,2]
print(set(l))

# Booleans
print(2 > 3)
print(3 <= 2)
print(3 == 2.0)
print(3.0 == 3)
print(4 ** 0.5 != 2)
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print(l_one[2][0] >= l_two[2]['k1'])