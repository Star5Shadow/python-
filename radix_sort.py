# 基数排序
def radix_sort(li):
    max_num = max(li)
    it = 0
    while 10**it <= max_num:
        buckets = [[]for _ in range(10)]
        for var in li:  # 分桶
            digit = (var // 10 ** it)%10
            buckets[digit].append(var)
        li.clear()
        for buc in buckets:
            li.extend(buc)
        it += 1


li = [1, 4, 5, 6, 6, 3, 4, 1, 6, 7, 7]
radix_sort(li)
print(li)