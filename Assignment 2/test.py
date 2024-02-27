def lcs(X, Y, m, n):
 
    # Declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]
 
    # Following steps build L[m+1][n+1] in bottom up fashion
    # Note: L[i][j] contains length of LCS of X[0..i-1]
    # and Y[0..j-1]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]

# Driver code
if __name__ == '__main__':
    a = [239, 27, 116, 26, 55, 214, 243, 43, 150, 96, 150, 45, 175, 236, 150, 206, 43, 115, 189, 32, 254, 255, 239, 16, 234, 254, 231, 234, 243, 220, 250, 242, 254, 153, 209, 225, 214, 32, 194, 185, 217, 249, 55, 250, 171, 209, 220, 254, 190, 94, 55, 147, 96, 104, 32]
    b = [27, 26, 147, 115, 243, 239, 16, 43, 234, 96, 190, 32, 45, 209, 175, 150, 206, 116, 254, 104, 189, 225, 236, 255, 231, 234, 254, 250, 254, 209, 214, 185, 217, 171, 249, 231, 220, 250, 94, 242, 153, 96, 185, 250, 55, 194, 32, 255]

    m = len(a)
    n = len(b)
    print("Length of LCS is", lcs(a, b, m, n))
