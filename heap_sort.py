# 堆排序算法
import random
def sift(li, low, high):
    """

    :param li: 列表
    :param low: 堆的艮节点位置
    :param high:堆的最后一个元素的位置
    :return:
    """
    i = low     # 根节点
    j = 2 * i + 1   # 左孩子
    tmp = li[low]
    while j <= high:    # 只要j位置有数就循环
        if j+1 <= high and li[j+1] > li[j]:
            j = j + 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j   # 往下看一层
            j = 2 * i + 1
        else:   # tmp更大则tmp放到i的位置上
            li[i] = tmp     # 把tmp放到某一位置
            break
    else:
        li[i] = tmp     # 把tmp放到叶子节点上


def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):   # i表示建堆的时候调整部分的根的下标
        sift(li, i, n-1)
    # 建堆完成了
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)    # i-1是新的high


li = [i for i in range(100)]
random.shuffle(li)
print(li)
heap_sort(li)
print(li)

