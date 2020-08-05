A = input()
B = input()
dp = [[0]*len(B) for i in range(len(A))]
for i in range(len(A)):
    for j in range(len(B)):
        if i==0 and j==0:
            if A[i] == B[j]:
                dp[i][j]=1
            else:
                dp[i][j] = 0
            continue
        if i==0:
            if A[i] == B[j]:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1]
            continue
        if j==0:
            if A[i] == B[j]:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j]
            continue
        
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            continue
        if A[i] != B[j]:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            continue
print(dp[i][j])