# 插入排序
def insert_sort(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i - 1
        while j>=0 and li[j]>tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp

li = [1,4,6,8,2,7,23,6]
insert_sort(li)
print(li)