# 搜索算法线性搜索和二分查找

def liner_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
        else:
            return None

def binary_search(li,val):
    left = 0
    right = len(li) - 1
    while left<=right:
        mid = (left+right)//2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else :
            left = mid + 1
    else:
        return None
