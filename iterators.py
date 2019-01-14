iterator = iter([i for i in range(10)])


while True:
    try:
        print(iterator.__next__())
    except StopIteration:
        break

print('finish iterator')


class CustomRange:

    def __init__(self, stop):
        self.curr = 0
        self.max = stop

    def __iter__(self):
        return CustomRange(self.max)

    def __next__(self):
        if self.curr < self.max:
            i = self.curr
            self.curr += 1
            return i
        else:
            raise StopIteration()


custom_iterator = CustomRange(5).__iter__()
while True:
    try:
        print(custom_iterator.__next__())
    except StopIteration as e:
        break
print('finish cumtom iterator')
