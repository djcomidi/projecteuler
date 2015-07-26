cubes_count = {}
cubes_lowest = {}
n = 1
while 5 not in list(cubes_count.values()):
    n3 = n ** 3
    key = ''.join(sorted(str(n3)))
    if key not in cubes_lowest:
        cubes_lowest[key] = n3
    cubes_count[key] = cubes_count.get(key, 0) + 1
    n += 1

for key, count in list(cubes_count.items()):
    if count == 5:
        result = cubes_lowest[key]
        print(result)
