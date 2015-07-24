from string import ascii_uppercase

from EulerTools import is_triangle


def is_triangle_word(w):
    return is_triangle(sum([ascii_uppercase.index(c) + 1 for c in w]))


with open('Problem042_words.txt') as in_file:
    words = in_file.readline()[1:-1].split('","')

count_triangles = 0
for word in words:
    if is_triangle_word(word):
        count_triangles += 1
print count_triangles
