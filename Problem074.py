from EulerTools import fac

FACS = [int(fac(i)) for i in xrange(10)]
memochains = {}


def sum_fac_digits(num):
    return sum(FACS[int(c)] for c in str(num))


def make_key(num):
    return ''.join(sorted(str(num).replace('0', '1')))


def chain_length(num):
    key = make_key(num)
    if key in memochains:
        return memochains[key]
    chain = []
    while (num not in chain) and (len(chain) <= 60):
        chain.append(num)
        num = sum_fac_digits(num)
    memochains[key] = len(chain)
    return len(chain)


chain_count = 0
for n in xrange(1, 10 ** 6):
    if chain_length(n) == 60:
        chain_count += 1
print chain_count
