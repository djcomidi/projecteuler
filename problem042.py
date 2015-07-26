from string import ascii_uppercase

from tools.euler import polygonal


def is_triangle_word(w):
    t = sum([ascii_uppercase.index(c) + 1 for c in w])
    n = int((2 * t) ** 0.5)
    return polygonal(3, n) == t


with open('problem042_words.txt') as in_file:
    words = in_file.readline()[1:-1].split('","')

count_triangles = 0
for word in words:
    if is_triangle_word(word):
        count_triangles += 1
print(count_triangles)
