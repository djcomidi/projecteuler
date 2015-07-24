from EulerTools import is_prime
from EulerTools import next_prime


def valid_prime(p):
    s = str(p)
    for i in xrange(1, len(s)):
        if not is_prime(int(s[:i])):
            return False
        if not is_prime(int(s[i:])):
            return False
    return True


p, total = 7, 0
for t in xrange(11):
    p = next_prime(p)
    while not valid_prime(p):
        p = next_prime(p)
    total += p
print total
