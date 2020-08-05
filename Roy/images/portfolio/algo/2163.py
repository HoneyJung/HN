def dp(n,m,x):
    if n==1 and m==1: 
        return x[0]
    if n > m :
        if n%2 == 0:
            dp(int(n/2),m,x)
            dp(int(n/2),m,x)
            x[0] = x[0] + 1
            return x[0]
        else:
            dp(int(n/2),m,x)
            dp(int(n/2) + 1,m,x)
            x[0] = x[0] + 1
            return x[0]
    else:
        if m%2 == 0:
            dp(n,int(m/2),x)
            dp(n,int(m/2),x)
            x[0] = x[0] + 1
            return x[0]
        else:
            dp(n,int(m/2),x)
            dp(n,int(m/2)+1,x)
            x[0] = x[0] + 1
            return x[0]
        
a,b = map(int, input().split())
x = [0]

print(dp(a,b,x))
