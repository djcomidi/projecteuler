from gmpy2 import is_square


def get_period(num):
    a, b, c = int(num ** 0.5), 1, int(num ** 0.5)
    confracs = []
    while not (a, b, c) in confracs:
        confracs.append((a, b, c))
        newb = (num - c ** 2) // b
        newa = int((num ** 0.5 + c) / newb)
        newc = abs(c - newb * newa)
        a, b, c = newa, newb, newc
    return len(confracs) - confracs.index((a, b, c))


count_odd = 0
for n in range(2, 10001):
    if not is_square(n):
        count_odd += get_period(n) & 1
print(count_odd)
