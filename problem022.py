from string import ascii_uppercase


def get_namescore(s):
    return sum(ascii_uppercase.index(c) + 1 for c in s)


with open('problem022_names.txt') as in_file:
    names = in_file.readline()[1:-1].split('","')
names.sort()
totalnamescore = 0
for i in range(len(names)):
    totalnamescore += (i + 1) * get_namescore(names[i])
print(totalnamescore)
