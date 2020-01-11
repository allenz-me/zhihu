from . import sort_decorator


def merge(l1: list, l2: list) -> list:
    """合并两个有序列表，可以用heapq.merge代替"""
    i, j, res = 0, 0, []
    length1, length2 = len(l1), len(l2)
    while i < length1 and j < length2:
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    if i < len(l1):
        res.extend(l1[i:])
    else:
        res.extend(l2[j:])
    return res


@sort_decorator
def mergeSort(nums: list) -> list:
    """归并排序"""
    if len(nums) <= 1:
        return nums
    if len(nums) == 2:
        return [min(nums), max(nums)]
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)
