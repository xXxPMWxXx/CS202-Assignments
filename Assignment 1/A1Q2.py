import sys
import math

'''
def gen_comb1(n:int, m:int, p:int, s:str):
    if p == n:
        if m == 0:
            combs.append(s)
    else:
        gen_comb1(n, m-1, p+1, s+char[p]) # with the character s[start]
        gen_comb1(n, m, p+1, s) # skip the character s[start]

char = 'abcdefghij'
n, m, combs = len(char), 3, []
gen_comb1(n, m, 0, '')
print(combs)

def gen_comb2(n:int, m:int, p:int, q:int, s:str):
    # n, m: generate all combinations of m from n numbers 0, 1, 2,..., n-1
    # p: from which position to start choosing next integer
    # q: number of remaining numbers to be chosen
    if q == 0:
        combs.append(s)
    else:
        for i in range(p, n-q+1):
            gen_comb2(n, m, i+1, q-1, s+char[i])

char = 'abcdefghij'
n, m, combs = len(char), 3, []
gen_comb2(n, m, 0, m, '')
print(combs)
'''
### code cannt pass OJ

# def p10_lines(n, m):
#     num_of_digits = len(str(math.comb(n, m)))
#     stop_value = 10 ** (num_of_digits - 1)
#     counter = 0
#     def gen_comb2(n: int, m: int, p: int, q: int, current_comb: list):
#         nonlocal counter 
#         if q == 0:
#             counter += 1
#             if math.log10(counter).is_integer(): # print those are log10, which is 1,10,100 ...
#                 result_str = ', '.join(map(str, current_comb))
#                 print(result_str)
#         else:
#             for i in range(p, n - q + 1):
#                 current_comb.append(i)
#                 if counter >= stop_value:
#                     return
#                 gen_comb2(n, m, i + 1, q - 1, current_comb)
#                 current_comb.pop()
#     gen_comb2(n, m, 0, m, [])


# refer from combinatorial number system 
def find_i_comb_recursive(i, n, m, index=None,current_comb=None, previous_number=None):
    if index == None: # initalize variables
        index = i
        current_comb = []
        previous_number = 0

    if len(current_comb) == m:
        result_str = ', '.join(map(str, current_comb))
        print(result_str)
        return

    curr_number = previous_number + 1
    while index > math.comb(n - curr_number, m - (len(current_comb) + 1)):
        index -= math.comb(n - curr_number, m - (len(current_comb) + 1))
        curr_number += 1

    current_comb.append(curr_number - 1)
    find_i_comb_recursive(i, n, m, index, current_comb, curr_number)
    
def p10_lines(n, m):
    num_of_digits = len(str(math.comb(n, m)))
    for i in range(0, num_of_digits):
        find_i_comb_recursive(10**i, n, m)

num_line = int(sys.stdin.readline())
gn, gc = 0, [[1]]
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    n, m = a[0], a[1]
    p10_lines(n, m)