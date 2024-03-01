# 桶排序的实现
def bucket_sort(li, n=100, max_num=10000):
    bucket = [[]for _ in range(n)]
    for var in li:
        i = min(var//(max_num//n), n-1)  # i表示var放到几号桶中
        bucket[i].append(var)
        for j in range(len(bucket[i])-1, 0, -1):
            if bucket[i][j] < bucket[i][j-1]:
                bucket[i][j], bucket[i][j-1] = bucket[i][j-1], bucket[i][j]
            else:
                break
    sorted_li = []
    for buc in bucket:
        sorted_li.extend(buc)
    return sorted_li


li = [23,4,1,63,62,41,13,5,6,25,67]
print(bucket_sort(li))
