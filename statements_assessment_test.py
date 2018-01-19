# 1
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)


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
for word in st.split():
    if len(word) % 2 == 0:
        print(word + ' <-- has an even number of letters')


# 5
for number in range(1,101):
    if number % 5 == 0 and number % 3 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)

# 6
st = 'Create a list of the first letters of every word in this string'
print([word[0] for word in st.split()])