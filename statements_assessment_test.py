# 1
st = 'Print only the words that start with s in this sentence'
# don't know

# 2
print(range(0,11,2))
even = [number for number in range(0,11) if number % 2 == 0]
print(even)

even2 = []
for number in range(0,11):
    if number % 2 == 0:
        even2.append(number)
        print(even2)

# 3
lst = [x for x in range(1,51) if x % 3 == 0]
print(lst)

# 4
st = 'Print every word in this sentence that has an even number of letters'
for letter in st:
    if letter % 2 == 0:

