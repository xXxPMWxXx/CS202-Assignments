import sys
lcslen = 0
# Method to get the longest bitonic sequence
def lbs(arr):
    n = len(arr)
    # allocate memory for LIS[] and initialize LIS values as 1
    # for all indexes
    lis = [1 for i in range(n+1)]
 
    # Compute LIS values from left to right
    for i in range(1 , n):
        for j in range(0 , i):
            if ((arr[i] > arr[j]) and (lis[i] < lis[j] +1)):
                lis[i] = lis[j] + 1
 
    # allocate memory for LDS and initialize LDS values for
    # all indexes
    lds = [1 for i in range(n+1)]
     
    # Compute LDS values from right to left
    for i in reversed(range(n-1)): #loop from n-2 downto 0
        for j in reversed(range(i-1 ,n)): #loop from n-1 downto i-1
            if(arr[i] > arr[j] and lds[i] < lds[j] + 1):
                lds[i] = lds[j] + 1

    # Return the maximum value of (lis[i] + lds[i] - 1)
    maximum = lis[0] + lds[0] - 1
    for i in range(1 , n):
        maximum = max((lis[i] + lds[i]-1), maximum)
    return maximum

def lcs(arr1, arr2, len1, len2, i, j,dp):
    if i == len1 or j == len2:
        dp[i][j] = 0
        return dp[i][j]
    if dp[i][j] != -1:
        return dp[i][j]
    if arr1[i] == arr2[j]:
        dp[i][j] = 1 + lcs(arr1, arr2, len1, len2, i + 1, j + 1,dp)
    else:
        dp[i][j] = max(lcs(arr1, arr2, len1, len2, i + 1, j,dp), lcs(arr1, arr2, len1, len2, i, j + 1,dp))
    return dp[i][j]


def getAllSubsequences(arr1, arr2, len1, len2, data, indx1, indx2, currlcs , dp , highest_common):
    if currlcs == lcslen:
        print(data[:currlcs])
        # To update the highest common subsequence
        current_common_count = lbs(data[:currlcs])
        print(current_common_count)
        if current_common_count > highest_common[0]:
            highest_common[0] = current_common_count
        return

    unique_elements = sorted(set(arr1[indx1:]) & set(arr2[indx2:]))
    for num in unique_elements:
        done = False
        for i in range(indx1, len1):
            if num == arr1[i]:
                for j in range(indx2, len2):
                    if num == arr2[j] and dp[i][j] == lcslen - currlcs:
                        data[currlcs] = num
                        getAllSubsequences(arr1, arr2, len1, len2, data, i + 1, j + 1, currlcs + 1, dp, highest_common)
                        done = True
                        break
                if done:
                    break

def LCMS(arr1, arr2):
    global lcslen
    len1, len2 = len(arr1), len(arr2)
    larger_len = max(len1, len2) + 1
    #dp for the lcs
    dp = [[-1 for _ in range(larger_len)] for _ in range(larger_len)]
    lcslen = lcs(arr1, arr2, len1, len2, 0, 0,dp)
    #date used to get all the subsequences
    data = [0 for _ in range(larger_len)]
    highest_common = [0]
    getAllSubsequences(arr1, arr2, len1, len2, data, 0, 0, 0,dp, highest_common)
    print(highest_common[0])

a = [239, 27, 116, 26, 55, 214, 243, 43, 150, 96, 150, 45, 175, 236, 150, 206, 43, 115, 189, 32, 254, 255, 239, 16, 234, 254, 231, 234, 243, 220, 250, 242, 254, 153, 209, 225, 214, 32, 194, 185, 217, 249, 55, 250, 171, 209, 220, 254, 190, 94, 55, 147, 96, 104, 32]
b = [27, 26, 147, 115, 243, 239, 16, 43, 234, 96, 190, 32, 45, 209, 175, 150, 206, 116, 254, 104, 189, 225, 236, 255, 231, 234, 254, 250, 254, 209, 214, 185, 217, 171, 249, 231, 220, 250, 94, 242, 153, 96, 185, 250, 55, 194, 32, 255]

LCMS(a,b)
# num_pair = int(sys.stdin.readline())

# for _ in range(num_pair):
#     a = [int(s) for s in sys.stdin.readline().split()]
#     b = [int(s) for s in sys.stdin.readline().split()]
#     common = set(a) & set(b)
#     a,b = [x for x in a if x in common], [x for x in b if x in common]
#     print(a)
#     print(b)
#     result = longest_common_subsequence(a, b)
#     print("--------------------------------")
#     print(result) 
#     print(lbs(result))
