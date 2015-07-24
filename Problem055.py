from EulerTools import is_palindrome


def is_lychrel(num):
    for i in xrange(50):
        num += int(str(num)[::-1])
        if is_palindrome(num):
            break
    return not is_palindrome(num)


lychrels = 0
for n in xrange(1, 10001):
    if is_lychrel(n):
        lychrels += 1
print lychrels
