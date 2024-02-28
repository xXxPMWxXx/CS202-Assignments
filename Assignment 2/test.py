import random

denom = [(1, 10), (2, 10), (3, 13), (7, 17), (14, 14), (29, 18), (57, 20), (115, 12), (231, 17), (462, 12)]

class MinCoin:
    def __init__(self, n, p):
        self.num_coin = n
        self.plan = [p]
    def add_plan(self, p):
        self.plan.append(p)

m = len(denom)
n = 10000

min_coin_with_plan = [None] * (n + 1)
min_coin_with_plan[0] = MinCoin(0, [0] * m)

for i in range(m - 1, -1, -1): ### Proposed correction for min_coin_with_plan
    for j in range(1, n+1): # consider the min coin problem with sum j cents
        if j >= denom[i][0] and min_coin_with_plan[j - denom[i][0]] is not None: # is it possible to use denom[i][0]? if yes, we can make up j cents by putting 1 coin of denom[i][0] and the min coin solution for j-denom[i][0]
            for p in min_coin_with_plan[j - denom[i][0]].plan: # for each possible plan of making j-denom[i][0]
                if p[i] < denom[i][1]: # now I have a better solution, build a new obj as a solution for j
                    if min_coin_with_plan[j] is None or min_coin_with_plan[j - denom[i][0]].num_coin + 1 < min_coin_with_plan[j].num_coin: # must check if there is enough supply of denom[i][0]
                        p_new = p.copy()
                        p_new[i] += 1 # add one coin of denom[i][0]
                        min_coin_with_plan[j] = MinCoin(min_coin_with_plan[j - denom[i][0]].num_coin + 1, p_new)
                    elif min_coin_with_plan[j - denom[i][0]].num_coin + 1 == min_coin_with_plan[j].num_coin: # now I have an equally good solution, only need to add the plan
                        p_new = p.copy()
                        p_new[i] += 1 # add one coin of denom[i][0]
                        min_coin_with_plan[j].add_plan(p_new)
for i in range(1, n+1):
    if min_coin_with_plan[i] is not None:
        print(i, min_coin_with_plan[i].num_coin, min_coin_with_plan[i].plan)

        