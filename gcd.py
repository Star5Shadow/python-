# 欧几里得算法，求最大公约数


def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(12,16))
