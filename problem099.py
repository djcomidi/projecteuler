from math import log

maxval = 0.0
maxline = 0
with open('problem099_base_exp.txt') as in_file:
    for i in range(1000):
        a, b = [int(x) for x in in_file.readline().strip().split(",")]
        val = float(b) * log(a)
        if val > maxval:
            maxval, maxline = val, i + 1
print(maxline)
