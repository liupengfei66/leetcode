# 先物品后背包
def test_1_wei_bag_problem():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4
    # 初始化: 全为0
    dp = [0] * (bag_weight + 1)

    # 先遍历物品, 再遍历背包容量
    for i in range(len(weight)):
        for j in range(bag_weight, weight[i] - 1, -1):
            # 递归公式
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp)

test_1_wei_bag_problem()

# 先背包，后物品
def test_2_wei_bag_problem():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4
    # 初始化: 全为0
    dp = [0] * (bag_weight + 1)
    # 如果正常初始化，是可以在一维数组时，也先背包，后物品的
    # 因为本质上也是用到的前数组
    for j in range(1, bag_weight+1):
        dp[j] = value[0]

    # 先遍历背包，再遍历物品
    for j in range(bag_weight, 0, -1):
        for i in range(1, len(weight)):
            # 递归公式
            if j >= weight[i]:
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp)

test_2_wei_bag_problem()