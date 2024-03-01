# 快速排序的实现

from cat_time import *
import random
import copy


@cal_time
def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            return


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:    # 从右边找比tmp小的数
            right -= 1  # 往左走一步
        li[left] = li[right]    # 把右边的值写到左边
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp    # 把tmp归位
    return left


def _quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        _quick_sort(li, left, mid-1)
        _quick_sort(li, mid+1, right)


@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li)-1)


li = list(range(10000))
random.shuffle(li)
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
quick_sort(li1)
bubble_sort(li2)