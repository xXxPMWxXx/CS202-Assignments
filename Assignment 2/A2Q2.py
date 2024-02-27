import sys

lcslen = 0
# Method to get the longest bitonic sequence
# Overall Time Complexity for longest_bitonic_subsequence method is : O(n^2), where n is the length of nums
def longest_bitonic_subsequence(nums):
    n = len(nums)

    increasing = [0] * n
    increasing[0] = 1
    # Time complexity: O(n^2)
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and increasing[j] > increasing[i]:
                increasing[i] = increasing[j]
        increasing[i] = increasing[i] + 1

    decreasing = [0] * n
    decreasing[n - 1] = 1
    # Time complexity: O(n^2)
    for i in reversed(range(n - 1)):
        for j in reversed(range(i + 1, n)):
            if nums[j] < nums[i] and decreasing[j] > decreasing[i]:
                decreasing[i] = decreasing[j]
        decreasing[i] = decreasing[i] + 1

    # check the max for increasing and decreasing
    max_lbs = 1
    # Time complexity: O(n)
    for i in range(n):
        max_lbs = max(max_lbs, increasing[i] + decreasing[i] - 1)
    return max_lbs

# refer from https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
# To get the longest common subsequence using memoization
# Time complexity: O(len1 * len2)
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

# Overall Time Complexity : O(u * m * n); 
# where 'u' is the length of the unique elements, when two input arrays are combined
# 'm' is the length of array 1
# 'n' is the length of array 2
# refer from https://www.geeksforgeeks.org/print-longest-common-sub-sequences-lexicographical-order/
def getAllSubsequences(arr1, arr2, len1, len2, data, indx1, indx2, currlcs, dp, highest_common):
    if currlcs == lcslen:
        # To update the highest common subsequence
        current_common_count = longest_bitonic_subsequence(data[:currlcs])
        if current_common_count > highest_common[0]:
            highest_common[0] = current_common_count
        return

    # combine the two arrays and get all the unique elements
    unique_elements = sorted(set(arr1[indx1:]) & set(arr2[indx2:]))
    # Time complexity for the nested loops : O(len_of_unique_elements * len1 * len2)
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
    #dp for the lcs 2D array of length larger_len
    dp = [[-1 for _ in range(larger_len)] for _ in range(larger_len)]
    lcslen = lcs(arr1, arr2, len1, len2, 0, 0, dp)
    #date used to store the longest common subsequences
    data = [-1 for _ in range(lcslen)]
    #To store the highest common mountain subsequences
    highest_common = [0]
    getAllSubsequences(arr1, arr2, len1, len2, data, 0, 0, 0, dp, highest_common)
    print(highest_common[0])

num_pair = int(sys.stdin.readline())
for _ in range(num_pair):
    a = [int(s) for s in sys.stdin.readline().split()]
    b = [int(s) for s in sys.stdin.readline().split()]
    # To only consider common elements in the given sequence, to improve the runtimes
    common = set(a) & set(b)
    a,b = [x for x in a if x in common], [x for x in b if x in common]
    LCMS(a,b)