n = int(input())
a = [x for x in input().split()]

dp1 = [1] * n
dp2 = [1] * n
#print(a)
for i in range(n):
    for j in range(i):
        if((a[i] > a[j]) and (dp1[i] < dp1[j] + 1)) : ####바꿔줘야할 때
            dp1[i] = dp1[j] + 1
        
for i in range(n-1,-1,-1):
    for j in range(i,n,1):
        if((a[i] > a[j]) and (dp2[i] < dp2[j] + 1 )):
            dp2[i] = dp2[j] + 1


M = 1
for i in range(n):
    if(dp1[i] + dp2[i] -1  > M):
        M = dp1[i] + dp2[i] - 1 

print(M)
#print(dp1,dp2)