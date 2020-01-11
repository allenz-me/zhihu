sort_algorithms = []


def sort_decorator(func):
    '''
    排序算法的装饰器
    用于将函数注册到列表 sort_algorithms 中
    '''
    sort_algorithms.append(func)
    return func


from .insertionSort import *
from .mergeSort import *
