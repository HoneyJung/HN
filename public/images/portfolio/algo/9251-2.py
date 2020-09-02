a = input()
b = input()

dp = [[0 for _ in range(len(b))] for _ in range(len(a))]
for i in range(len(a)):
    if b[0] == a[i]: 
        dp[i][0] = 1
        continue
    if i > 0:
        dp[i][0] = dp[i-1][0]

for i in range(len(b)):
    if a[0] == b[i]: 
        dp[0][i] = 1
        continue
    if i > 0:
        dp[0][i] = dp[0][i-1]


#print(dp)
for i in range(1,len(a)):
    for j in range(1,len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])

#print(dp)
print(dp[len(a)-1][len(b)-1])