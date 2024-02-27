import random

# Assuming the denominations and their quantities are given
denom = [(1,  10), (2,  10), (3,  13), (7,  17), (14,  14), (29,  18), (57,  20), (115,  12), (231,  17), (462,  12)]

# Initialize the minimum number of coins needed for each amount up to n
n =  7000
min_coin_with_plan = [None] * (n +  1)
min_coin_with_plan[0] = (0, [0] * len(denom))  # No coins needed for  0

# Iterate through each denomination
for i in range(len(denom)):
    for j in range(1, n +  1):
        if j >= denom[i][0] and min_coin_with_plan[j - denom[i][0]] is not None:
            # Check if using the current denomination is better
            if min_coin_with_plan[j] is None or min_coin_with_plan[j - denom[i][0]][0] +  1 < min_coin_with_plan[j][0]:
                # Create a new plan using the current denomination
                new_plan = min_coin_with_plan[j - denom[i][0]][1].copy()
                new_plan[i] +=  1  # Increase the count of the current denomination
                min_coin_with_plan[j] = (min_coin_with_plan[j - denom[i][0]][0] +  1, new_plan)
            elif min_coin_with_plan[j - denom[i][0]][0] +  1 == min_coin_with_plan[j][0]:
                # If the number of coins is the same, add the new plan
                new_plan = min_coin_with_plan[j - denom[i][0]][1].copy()
                new_plan[i] +=  1
                min_coin_with_plan[j][1].append(new_plan)

# For n =  6006, find the minimum number of coins
if min_coin_with_plan[6005] is not None:
    print(f"Minimum number of coins for  6006: {min_coin_with_plan[6006][0]}")
else:
    print("No solution found for  6006.")
