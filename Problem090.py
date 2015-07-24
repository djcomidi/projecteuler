from itertools import combinations

from EulerTools import is_square


def testdice(facesa, facesb):
    seta, setb = set(facesa), set(facesb)
    if 6 in facesa or 9 in facesa:
        seta |= {6, 9}
    if 6 in facesb or 9 in facesb:
        setb |= {6, 9}
    numbers = set()
    for faceA in seta:
        for faceB in setb:
            numbers.add(10 * faceA + faceB)
            numbers.add(10 * faceB + faceA)
    squares = filter(lambda num: num > 0 and is_square(num), numbers)
    return len(squares) == 9


facesList = [map(int, faces) for faces in combinations("0123456789", 6)]
arrangements = 0
for i, facesA in enumerate(facesList):
    for facesB in facesList[i + 1:]:
        if testdice(facesA, facesB):
            arrangements += 1
print arrangements
