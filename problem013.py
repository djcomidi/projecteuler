the_sum = 0
with open('problem013_data.txt') as in_file:
    for line in in_file.readlines():
        the_sum += int(line[:-1])
solution = str(the_sum)[:10]
print(solution)
