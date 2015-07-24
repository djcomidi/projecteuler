the_sum = 0
with open('Problem013_data.txt') as in_file:
    for line in in_file.readlines():
        the_sum += int(line[:-1])
print str(the_sum)[:10]
