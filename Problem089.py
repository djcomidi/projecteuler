ROMANS = "I,IV,V,IX,X,XL,L,XC,C,CD,D,CM,M".split(",")
VALUES = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]


def roman_to_western(roman):
    western, idx = 0, 0
    while idx < len(roman):
        if roman[idx:idx + 2] in ROMANS:
            d = 2
        else:
            d = 1
        t = ROMANS.index(roman[idx:idx + d])
        western += VALUES[t]
        idx += d
    return western


def western_to_roman(western):
    roman = ""
    while western > 0:
        n = max([v for v in VALUES if v <= western])
        roman += ROMANS[VALUES.index(n)]
        western -= n
    return roman


with open('Problem089_roman.txt') as in_file:
    romans = [line.strip() for line in in_file.readlines()]

savings = 0
for r in romans:
    w = roman_to_western(r)
    romanshort = western_to_roman(w)
    savings += len(r) - len(romanshort)
print(savings)
