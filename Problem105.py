def get_subsets(a):
    subsets = []
    for i in xrange(1, 2 ** len(a)):
        subsets.append(set(a[j] for j in xrange(len(a)) if i & (2 ** j) > 0))
    return subsets


def is_special_set(a):
    subsets = get_subsets(a)
    subsets.sort(key=len)
    for iB, subsetB in enumerate(subsets):
        sumb, lenb = sum(subsetB), len(subsetB)
        for subsetC in subsets[:iB]:
            sumc, lenc = sum(subsetC), len(subsetC)
            if not subsetB.isdisjoint(subsetC):
                continue
            if sumb == sumc:
                return False
            if lenb > lenc and sumb <= sumc:
                return False
    return True


sumspecials = 0
with open('Problem105_sets.txt') as in_file:
    for line in in_file.readlines():
        arr = map(int, line.strip().split(','))
        if is_special_set(arr):
            sumspecials += sum(arr)
print sumspecials
