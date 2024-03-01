# 活动的选择，保证能参与的活动数量最大

activities = [(1,4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]      #   表示活动的开始时间和结束时间
# 保证活动是按结束时间排好序的
activities.sort(key=lambda x: x[1])


def activities_selection(a):
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i][0] >= res[-1][1]:
            res.append(a[i])
    return res


print(activities_selection(activities))
