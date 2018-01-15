my_dict = {'key1':'value','key2':'value2'}
print(my_dict['key1'])
my_dict = {'k1':123,'k2':3.4,'k3':'string'}
print(my_dict['k3'][::-1].upper())
print(my_dict['k1'] - 120)
my_dict['k1'] = my_dict['k1'] - 120
print(my_dict['k1'])
print(my_dict)
my_dict['k1'] = my_dict['k1'] + 100
print(my_dict['k1'])
my_dict['k1'] += 101
print(my_dict['k1'])
d = {}
print(d)
d['animal'] = 'Dog'
d['answer'] = 42
print(d)
d = {'k1': {'nestkey': {'subnestkey': 'value'}}}
print(d)
print(d['k1']['nestkey']['subnestkey'].upper())
d = {}
d['k1'] = 1
d['k2'] = 2
d['k3'] = 3
print(d)
d.keys()
print(d)
d.values()
print(d)
print(d['k1'])
d.items()
print(d)