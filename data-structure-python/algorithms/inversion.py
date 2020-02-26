import bisect

def inversions_brute(l: list) -> int:
    res = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                res += 1
    return res

def merge(l1, l2):
    i, j = 0, 0
    res, inv = [], 0
    length1, length2 = len(l1), len(l2)
    while i < length1 and j < length2:
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
            inv += length1 - i
    if i < len(l1):
        res.extend(l1[i:])
    else:
        res.extend(l2[j:])
    return res, inv

def inversions_merge(l :list):
    if len(l) <= 1:
        return l, 0
    elif len(l) == 2:
        return [min(l), max(l)], 0 if l[0]<=l[1] else 1
    mid = len(l) // 2
    left,a=inversions_merge(l[:mid])
    right,b=inversions_merge(l[mid:])
    r, inv = merge(left, right)
    return r, inv + a + b

def inversions_bisect(l: list) -> int:
    ri, res = [], 0
    for i in reversed(range(0, len(l))):
        bs = bisect.bisect_left(ri, l[i])
        res += bs
        ri.insert(bs, l[i])
    return res


def update(arr: list, p: int):
    while p < len(arr):
        arr[p] += 1
        p += (-p) & p

def getSum(arr: list, p: int) -> int:
    res = 0
    while p:
        res += arr[p]
        p -= (-p) & p
    return res

def discrete(l: list) -> list:
    """将数组离散化"""
    s = set(l)
    d = dict(zip(sorted(s), range(1, len(s)+1)))
    for i in range(len(l)):
        l[i] = d[l[i]]
    return l

def inversion_bit(l: list) -> int:
    res, l = 0, discrete(l)
    arr = [0] * (len(l) + 1)
    for i, n in enumerate(l, start=1):
        update(arr, n)
        res += i - getSum(arr, n)
    return res

if __name__ == '__main__':
    arr = [3, 2, 4, 1, 5]
    print(inversions_bisect(arr))
    print(inversion_bit(arr))