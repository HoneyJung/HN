import sys
sys.setrecursionlimit(100000)
""" 
def dp(mat,a,b):
    if a == 1 and b == 1:
        return mat[0][0]
    if a==1:
        return dp(mat,a,b-1) + mat[a-1][b-1]
    if b==1:
        return dp(mat,a-1,b) + mat[a-1][b-1]
        
    return max(dp(mat,a-1,b),dp(mat,a,b-1),dp(mat,a-1,b-1)) + mat[a-1][b-1]
"""

N,M = map(int,input().split())
mat = [[int(x) for x in input().split()] for y in range(N)]
dp = [[0]*(M+1) for i in range(N+1)]

for i in range(N):
    for j in range(M):
        if i==0 and j==0:
            dp[i][j] = mat[i][j]
            continue
        if i == 0:
            dp[i][j] = dp[i][j-1] + mat[i][j]
            continue
        if j == 0:
            dp[i][j] = dp[i-1][j] + mat[i][j]
            continue
        dp[i][j] = max(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + mat[i][j]
print(dp)
print(dp[N-1][M-1])