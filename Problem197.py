from math import floor


def func(x):
    return floor(2 ** (30.403243784 - x ** 2)) * 10 ** -9


uList = []
uVal = -1
while uVal not in uList:
    uList.append(uVal)
    uVal = func(uVal)
print sum(uList[-2:])
