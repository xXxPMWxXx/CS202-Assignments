import math


def find_i_comb(i,n, m): # refer from wiki combinatorial number system
    current_comb = []
    index = i
    minus_number = 0

    for j in range(1, m + 1):
        curr_number = minus_number +1
        while index - math.comb(n - curr_number, m - j) > 0:
            index -= math.comb(n - curr_number, m - j)
            curr_number += 1
        current_comb.append(curr_number - 1)
        minus_number = curr_number # update the number for n to minus from
    # print the i-th combination
    result_str = ', '.join(map(str, current_comb))
    print(result_str)

find_i_comb(100, 20, 10)


def find_i_comb_recursive(i, n, m, index=None,current_comb=[], minus_number=0):
    if index == None:
        index = i

    if len(current_comb) == m:
        result_str = ', '.join(map(str, current_comb))
        print(result_str)
        return

    curr_number = minus_number + 1
    while index - math.comb(n - curr_number, m - (len(current_comb) + 1)) > 0:
        index -= math.comb(n - curr_number, m - (len(current_comb) + 1))
        curr_number += 1

    current_comb.append(curr_number - 1)
    minus_number = curr_number
    find_i_comb_recursive(i, n, m, index, current_comb, minus_number)

find_i_comb_recursive(10,5,2)