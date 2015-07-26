for n in range(1, 20):
    for m in range(n + 1, 20):
        a, b, c = (m ** 2 - n ** 2), 2 * m * n, (m ** 2 + n ** 2)
        for k in range(1, 100):
            ka, kb, kc = k * a, k * b, k * c
            if ka + kb + kc == 1000:
                product = ka * kb * kc
                print(product)
                break
