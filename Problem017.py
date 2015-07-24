# http://en.wikipedia.org/wiki/English-language_numerals

NAMES = ["", "one", "two", "three", "four", "five",
         "six", "seven", "eight", "nine", "ten",
         "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]


def get_full(number):
    if number == 1000:
        return "onethousand"
    name = ""
    h, td = divmod(number, 100)
    if h > 0:
        name += NAMES[h] + "hundred"
    if td > 0:
        if len(name) > 0:
            name += "and"
        if td < 20:
            name += NAMES[td]
        else:
            t, d = divmod(td, 10)
            name += TENS[t]
            name += NAMES[d]
    return name


letters = 0
for n in xrange(1, 1001):
    letters += len(get_full(n))
print letters
