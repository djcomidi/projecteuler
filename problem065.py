def get_part(n):
    if n == 1:
        return 2
    if n % 3 == 0:
        return 2 * (n // 3)
    else:
        return 1


def get_term(i):
    nom, denom = get_part(i), 1
    while i > 1:
        i -= 1
        p = get_part(i)
        nom, denom = p * nom + denom, nom
    return nom, denom


n, d = get_term(100)
sumd = sum([int(x) for x in str(n)])
print(sumd)
