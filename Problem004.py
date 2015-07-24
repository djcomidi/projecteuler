from EulerTools import is_palindrome

max_palin = 0
for a in xrange(900, 1000):
    for b in xrange(a, 1000):
        t = a * b
        if is_palindrome(t):
            max_palin = max(max_palin, t)
print max_palin
