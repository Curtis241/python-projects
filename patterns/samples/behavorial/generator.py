# Build and return a list
def firstn_without_yield(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums


# Using the generator pattern (an iterable)
class firstn_using_iter(object):
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()


# a generator that yields items instead of returning a list
def firstn_with_yield(n):
    num = 0
    while num < n:
        yield num
        num += 1


# Note: Python 2.x only
# using a non-generator
print(sum(range(1000000)))

print(sum(firstn_using_iter(1000000)))
print(sum(firstn_without_yield(1000000)))
print(sum(firstn_with_yield(1000000)))