# 贪心算法——背包问题：每次优先拿取单位价值最高的物品
goods = [(60,10),(120,30),(100,20)] # 每个商品元组表示价格和重量
goods.sort(key=lambda x: x[0]/x[1], reverse=True)


def fractional_backpack(goods, w):
    m = [0 for _ in range(len(goods))]
    total_v = 0
    for i,(price,wight) in enumerate(goods):
        if w >= wight:
            m[i] = 1
            w -= wight
            total_v += price
        else:
            m[i] = w/wight
            total_v += m[i]*price
            w = 0
            break
    return total_v, m


print(fractional_backpack(goods,50))
