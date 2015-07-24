funcA = lambda n: n ** 3
funcB = lambda n: sum((-n) ** e for e in xrange(11))


def lagrange_term(k, n):
    # (x0,y0),...,(xk,yk)
    term = 0.0
    # L(x) = sum( y_j*l_j(x) , 0<=j<=k )
    for j in xrange(n):
        base = 1.0
        # l_j(x) = prod( (x-x_m)/(x_j-x_m) , 0<=m<=k and m!=j )
        for m in xrange(k + 1):
            if m == j:
                continue
            base *= float(n - m) / float(j - m)
        term += funcB(j + 1) * base
    return term


total = 0
for i in xrange(10):
    total += lagrange_term(i, i + 1)
print total
