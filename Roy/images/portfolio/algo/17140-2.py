import sys
r,c,k = map(int,sys.stdin.readline().split())
M = [[int(a) for a in sys.stdin.readline().split()] for i in range(3)]
#print(r,c)
#print(M)
m,n = 3,3
time = 0
#print(M)
while(time<101):
    #print(M[r-1][c-1])
    #print(r,c)
    #print(len(M),len(M[0]))
    if r-1 < len(M) and c-1 < len(M[0]):
        #print("hi")
        #print(M[r-1][c-1], k)
        if M[r-1][c-1] == k:
            break
    MM = []
    #print(M)

    flag = 0
    if len(M)<len(M[0]): # 열이 더 짧으면 transpose
        M=list(zip(*M))
        flag = 1
    
    for i in range(len(M)):
        L = {}
        for j in range(len(M[0])):
            #print(j)
            if M[i][j] == 0:
                continue
            if M[i][j] in L.keys():
                L[M[i][j]] = L[M[i][j]] + 1
            else:
                L[M[i][j]] = 1
        #######################################################
        #print(L)
        MAX = max(L.values()) + 1 
        LL = [[] for _ in range(MAX)]
        #print(LL)
        for j in (L.keys()):
            LL[L[j]].append(j)
            LL[L[j]].sort()
        #print(LL)
        ###########################################################
        MM.append([])
        for j in range(1,len(LL)):
            for t in (LL[j]):
                MM[i].append(t)
                MM[i].append(j)
    # 0 맞춰주기.
    Max = 0
    for i in range(len(MM)):
        if Max < len(MM[i]):
            Max = len(MM[i])
    for i in range(len(MM)):
        for j in range(len(MM[i]),Max):
            MM[i].append(0)
    
    M = MM
    if flag == 1:
        M=list(zip(*M))
    #print(M)
    time = time + 1

if time ==101:
    print(-1)
else:
    print(time)