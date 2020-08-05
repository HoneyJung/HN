import sys

a = int(input())

T = [0]*15
P = [0]*15
#F = [0]*15
k = 0
temp = 0
dp = [0]*15
for i in range(a):
    T[i],P[i] = map(int,input().split())

########## 범위 넘어가는거 전처리
for i in range(a):
    if T[i] + i > a:
        P[i] = -100000 
#print("P")
#print(P)
for i in range(a):
    if i == 0: ############첫번째
        dp[i] = P[i]
        k = T[i]
        temp = P[i]
        continue
    if k <= i: ############원래있던거랑 공존 가능한경우.
        dp[i] = dp[i-1] + P[i]
        temp = P[i]
        k = k + T[i]
        continue
    else:
        if dp[i-1] - temp + P[i] >  dp[i-1]: #####새거 하는게 이득인경우
            dp[i] = dp[i-1] - temp + P[i]
        else:
            dp[i] = dp[i-1]
            
print((dp))

    
    
    
