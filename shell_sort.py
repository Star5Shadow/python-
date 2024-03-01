# 希尔排序
def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j>=0 and li[j]>tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp


def shell_sort(li):
    d = len(li)//2
    while d>=1:
        insert_sort_gap(li, d)
        d //= 2


li = [3, 5, 2, 6, 7, 1, 3, 5, 7]
shell_sort(li)
print(li)

