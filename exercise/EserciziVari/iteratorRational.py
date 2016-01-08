import random


class RandomInteger():

    def __init__(self, maxvalue):
        self.max = maxvalue

    def __iter__(self):
        self.count = 0
        random.seed(1)
        return self

    def __next__(self):
        if self.count < self.max:
            randomInteger = random.randint(0, self.max)
            self.count += 1
            return randomInteger
        else:
            raise StopIteration


if __name__ == '__main__':
    iterator = RandomInteger(100)
    print([value for value in iterator])
