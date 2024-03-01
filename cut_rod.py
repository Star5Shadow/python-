# 动态规划问题——钢条切割
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


# 自顶向下的实现，时间复杂度为2的指数级
def cut_rod_recurision_1(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_recurision_1(p, i)+cut_rod_recurision_1(p, n-i))      # 砍一刀，两段钢条的最大价格之和
        return res


def cut_rod_recurision_2(p, n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1,n+1):
            res = max(res, p[i]+cut_rod_recurision_2(p,n-i))    # 假定最小第一刀的位置，后面部分取最大价值
        return res


# 自底向上的实现
def cut_rod_dp(p, n):
    r = [0]
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n+1):
            for j in range(1, i+1):
                res = max(res, p[j] + r[i-j])
            r.append(res)
        return res


def cut_rod_extend(p, n):
    r = [0]
    s = [0]
    if n == 0:
        return 0
    else:
        res_r = 0    # 价格的最大值
        res_c = 0    # 价格最大值所对应的左边一刀
        for i in range(1, n+1):
            for j in range(1, i+1):
                if res_r < p[j] + r[i-j]:
                    res_r = p[j] + r[i-j]
                    res_c = j
            r.append(res_r)
            s.append(res_c)
        return r[n], s


def cut_rod_solution(p, n):
    r, s = cut_rod_extend(p, n)
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return ans


print(cut_rod_dp(p, 9))
print(cut_rod_solution(p,9))