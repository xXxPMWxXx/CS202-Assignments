import sys

# Refer from : https://medium.com/@florian_algo/unveiling-the-bounded-knapsack-problem-737d71c4146b
# Since the items_len is O(N * log(max_quantity)
# Therefore, the overall time complexity is O(N * log(max_quantity) * limit)
def bounded_knapsack(weight, value, quantity, limit):
    # e.g. if the item quantity is 10, it will be spilted to 4 new items, as quantity: 1(2^0), 2(2^1), 4(2^2), 2(remaining quantity)
    # Since there are N items , and for each item the complexity will be log(max_quantity)
    # Therefore, overall Time complexity of this section will be: O(N * log(max_quantity))
    items = []
    N = len(weight)
    for i in range(N):
        current_weight = weight[i]
        current_value = value[i]
        current_quantity = quantity[i]
        k = 1
        while k <= current_quantity:
            items.append((current_weight * k, current_value * k))
            current_quantity -= k
            k *= 2
        if current_quantity > 0:
            # Store the weight and value in items
            items.append((current_weight * current_quantity, current_value * current_quantity))

    #Bottom up approach; The time complexity of this section wil be O(items_len * limit)
    items_len = len(items)
    dp = [[0 for _ in range(limit + 1)] for _ in range(items_len + 1)]
    for i in range(1, items_len + 1):
        for w in range(1, limit + 1):
            cur_weight, cur_value = items[i-1]
            if cur_weight <= w:
                dp[i][w] = max(cur_value + dp[i - 1][w - cur_weight], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[items_len][limit]

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()]
    print(bounded_knapsack([i[0] for i in a[:-1]], [i[1] for i in a[:-1]], [i[2] for i in a[:-1]], a[-1][0]))
