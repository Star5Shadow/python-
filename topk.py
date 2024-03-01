# topk问题，最大的前几个数
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
        if j+1 <= high and li[j+1] < li[j]:
            j = j + 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j   # 往下看一层
            j = 2 * i + 1
        else:   # tmp更大则tmp放到i的位置上
            li[i] = tmp     # 把tmp放到某一位置
            break
    else:
        li[i] = tmp     # 把tmp放到叶子节点上


def topk(li,k):
    heap = li[0:k]
    # 1.建堆
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)

    # 2.遍历
    for i in range(k,len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)

    # 3.出数
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)

    return heap


import random
li = list(range(1000))
random.shuffle(li)
print(topk(li, 10))
