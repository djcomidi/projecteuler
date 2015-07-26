from tools.euler import is_palindrome

solutions = set()
for start in range(1, 10 ** 4):
    length = 0
    val = start ** 2
    while True:
        length += 1
        val += (start + length) ** 2
        if val > 10 ** 8:
            break
        if is_palindrome(val):
            solutions.add(val)
total = sum(solutions)
print(total)
