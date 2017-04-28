import random


def even(a):
    even_numbers = []
    for i in range(0,21,2):
        b = a + i
        even_numbers.append(b)
    return even_numbers

def minMax():
    digits = [4,63,2,6,8,68,7,2,98,43,1,2,47,87,9]
    return sum(digits)

def count():
    for i in range(1,21):
        print i

def oneMil():
    milli = []
    for i in range(1, 1000001):
        milli.append(i)
    print min(milli)
    print max(milli)
    print sum(milli)

def odd():
    for i in range(1,21,2):
        print i

def three():
    multi = []
    for i in range(3,31):
        if i % 3 == 0:
            multi.append(i)
    for b in multi:
        print b

def cube():
    list = [value**3 for value in range(1,11)]
    for i in list:
        print i


class Lotterie:
    def __init__(self):
        self.lotogrid = []
        self.lotopick = []



    def grid(self):
        for i in range(20):
            randomnum = random.randint(0, 51)
            self.lotogrid.append(randomnum)

    def loto(self):
        for i in range (5):
            lotonum = random.randint(0, 51)
            self.lotopick.append(lotonum)

match = Lotterie
match.grid()