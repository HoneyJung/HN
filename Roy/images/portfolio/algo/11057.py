n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n)]
for i in range(10):
    dp[0][i] = 1

for i in range(1,n):
    for j in range(10):
        for k in range(0,j+1):
            dp[i][j] = dp[i][j] + dp[i-1][k]

summ = 0
for i in range(10):
    summ = summ + dp[n-1][i]
print(summ%10007)