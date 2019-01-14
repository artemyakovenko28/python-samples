def number_generator(stop):
    for i in range(stop):
        yield i


iterator = number_generator(5)

while True:
    try:
        print(iterator.__next__())
    except StopIteration:
        break

# the same
# for i in number_generator(5):
#     print(i)

print('end generator iteration')


fruits = ['apple', 'banana', 'cherry']
print(fruits[0])

c = {'a', 'b'}
c.remove('a')

s = {}
del s['a']

