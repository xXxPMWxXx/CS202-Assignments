import sys
import time 
#refer from : https://medium.com/@florian_algo/unveiling-the-bounded-knapsack-problem-737d71c4146b
def bounded_knapsack(weight, value, quantity, limit):
    # bruce force: Time complexity: O(weight * limit * max_qty)
    # start_time = time.time()
    # # Number of items
    # N = len(weight)
    # # Initialize DP table
    # dp = [[0 for _ in range(limit + 1)] for _ in range(N + 1)]

    # # Build the table dp[][] in bottom-up manner
    # for i in range(1, N + 1):
    #     for w in range(1, limit + 1):
    #         max_qty = min(quantity[i-1], w // weight[i-1])  # Maximum quantity of the i-th item that can be included
    #         for q in range(max_qty + 1):  # loop all possible quantities of the i-th item
    #             remaining_weight = w - (q * weight[i-1])
    #             dp[i][w] = max(dp[i][w], dp[i-1][remaining_weight] + q * value[i-1])
    # print("--- %s seconds spent ---" % (time.time() - start_time))
    # return dp[N][limit]
    
    # Time complexity: O(N * limit  * log(max value of the i-th item))
    start_time = time.time()
    # To generate new items, 
    # e.g. if the item quantity is 10, it will be spilted to 4 new items, as quantity: 1(2^0), 2(2^1), 4(2^2), 2(remaining quantity)
    items = []
    for i in range(len(weight)):
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

    # Space optimization for 0/1 approach
    # result = [0] * (limit + 1)

    # # Solve the 0/1 knapsack problem
    # for weight, value in items:
    #     for j in range(limit, weight - 1, -1):
    #         result[j] = max(result[j], result[j - weight] + value)
    # print("--- %s seconds spent ---" % (time.time() - start_time))
    # return result[limit]
   
    #bottom up approach
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
