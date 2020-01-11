from . import sort_decorator


@sort_decorator
def insertionSort(nums: list) -> list:
    """插入排序"""
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums
