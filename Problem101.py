def func_b(n):
    return sum((-n) ** e for e in range(11))


def lagrange_term(k, n):
    # (x0,y0),...,(xk,yk)
    term = 0.0
    # L(x) = sum( y_j*l_j(x) , 0<=j<=k )
    for j in range(n):
        base = 1
        # l_j(x) = prod( (x-x_m)/(x_j-x_m) , 0<=m<=k and m!=j )
        for m in range(k + 1):
            if m == j:
                continue
            base *= (n - m) / (j - m)
        term += func_b(j + 1) * base
    return term


total = 0
for i in range(10):
    total += lagrange_term(i, i + 1)
result = int(total)
print(result)
