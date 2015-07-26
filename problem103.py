setA = [11, 18, 20, 22, 25]
setB = [setA[len(setA) // 2]]
for i in range(len(setA)):
    setB.append(setB[0] + setA[i])
result = ''.join([str(x) for x in setB])
print(result)
