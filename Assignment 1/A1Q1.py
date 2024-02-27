import sys
#Recursive
# with reference from CS201(W4): recursive implementation for power(in-class ex #2)
def power_modulo(m, k, n):
    
    if m == 0: # 0^n = 0
        return 0
    if k == 0: # n^0 = 1
        return 1

    split = power_modulo(m, k//2 ,n) # every iteration, halved => O(log k)

    if k % 2 == 0: # for k is even
        return (split * split) % n # associative law
    else : # k is odd
        return  (split * split * m) % n 

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    m, k, n = a[0], a[1], a[2]
    print(power_modulo(m, k, n))