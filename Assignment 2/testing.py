MAX = 100
lcslen = 0

# dp matrix to store result of sub calls for lcs
dp = [[-1 for i in range(MAX)] for i in range(MAX)]

# A memoization based function that returns LCS of
# arr1[i..len1-1] and arr2[j..len2-1]
def lcs(arr1, arr2, len1, len2, i, j):

    # base condition
    if i == len1 or j == len2:
        dp[i][j] = 0
        return dp[i][j]

    # if lcs has been computed
    if dp[i][j] != -1:
        return dp[i][j]

    ret = 0
    if arr1[i] == arr2[j]:
        ret = 1 + lcs(arr1, arr2, len1, len2, i + 1, j + 1)
    else:
        ret = max(lcs(arr1, arr2, len1, len2, i + 1, j),
                  lcs(arr1, arr2, len1, len2, i, j + 1))
    dp[i][j] = ret
    return ret

# Function to print all LCS of arr1 and arr2 of length lcslen
def printAll(arr1, arr2, len1, len2, data, indx1, indx2, currlcs):
    if currlcs == lcslen:
        print(data[:currlcs])
        return

    if indx1 == len1 or indx2 == len2:
        return

    unique = sorted(set(arr1[indx1:]) & set(arr2[indx2:]))
    for num in unique:
        done = False
        for i in range(indx1, len1):
            if num == arr1[i]:
                for j in range(indx2, len2):
                    if num == arr2[j] and dp[i][j] == lcslen - currlcs:
                        data[currlcs] = num
                        printAll(arr1, arr2, len1, len2, data, i + 1, j + 1, currlcs + 1)
                        done = True
                        break
                if done:
                    break

# This function prints all LCS of arr1 and arr2 in sorted order.
def prinlAllLCSSorted(arr1, arr2):
    global lcslen
    len1, len2 = len(arr1), len(arr2)

    lcslen = lcs(arr1, arr2, len1, len2, 0, 0)

    # Print all LCS using recursive backtracking
    data = [0 for i in range(MAX)]
    printAll(arr1, arr2, len1, len2, data, 0, 0, 0)

# Driver program to run the case
if __name__ == '__main__':
    a = [239, 27, 116, 26, 55, 214, 243, 43, 150, 96, 150, 45, 175, 236, 150, 206, 43, 115, 189, 32, 254, 255, 239, 16, 234, 254, 231, 234, 243, 220, 250, 242, 254, 153, 209, 225, 214, 32, 194, 185, 217, 249, 55, 250, 171, 209, 220, 254, 190, 94, 55, 147, 96, 104, 32]
    b = [27, 26, 147, 115, 243, 239, 16, 43, 234, 96, 190, 32, 45, 209, 175, 150, 206, 116, 254, 104, 189, 225, 236, 255, 231, 234, 254, 250, 254, 209, 214, 185, 217, 171, 249, 231, 220, 250, 94, 242, 153, 96, 185, 250, 55, 194, 32, 255]

    prinlAllLCSSorted(a, b)
