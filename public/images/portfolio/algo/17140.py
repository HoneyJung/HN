import sys
r,c,k = map(int,sys.stdin.readline().split())
M = [[int(a) for a in sys.stdin.readline().split()] for i in range(3)]

#print(M)
m,n = 3,3
flag = 0
count = 0
flag2 = 1
while(1):
    xxx = m
    if flag2 == 1 and r-1 < m and c-1 < n:
        if M[r-1][c-1] == k:
            break
    if flag2 == -1 and c-1 < m and r-1 < n:
        if M[c-1][r-1] == k:
            break
    count = count + 1
    #print(count)
    if count > 100:
        print(-1)
        flag =10
        break
    #print(m,n)
    if flag2 == -1 and m == n:
        xxx = m
        m = 0
    if m >= n:
        flag = 0
        for i in range(m):
            dic = {}
            L = [[] for _ in range(101)]
            for j in range(n):
                if M[i][j] == 0:
                    continue
                if M[i][j] in dic.keys():
                    #print("key : ",j)
                    #print(M[i][j])
                    dic[M[i][j]] = dic[M[i][j]] + 1
                else:
                    #print("첫")
                    dic[M[i][j]] = 1
            #print(dic)
            for t in dic.keys():
                L[dic[t]].append(t)
                L[dic[t]].sort()
            #print("L : ",L[:3][:3])
            # change to new one
            temp = []
            for ii in range(len(L)):
                if ii == 0:
                    continue
                for jj in range(len(L[ii])):
                    temp.append(L[ii][jj])
                    temp.append(ii) 
            #print(temp)
            M[i] = temp

    else:
        m = xxx
        flag2 = flag2 * -1
        flag = 1
        temp = [[] for _ in range(n)]
        for i in range(n):
            dic = {}
            L = [[] for _ in range(101)]
            for j in range(m):
                if M[j][i] == 0:
                    continue                
                if M[j][i] in dic.keys():
                    #print("key : ",j)
                    #print(M[i][j])
                    dic[M[j][i]] = dic[M[j][i]] + 1
                else:
                    #print("첫")
                    dic[M[j][i]] = 1

            for t in dic.keys():
                L[dic[t]].append(t)
                L[dic[t]].sort()
            #print("L : ",L)    
            for t in range(len(L)):
                for j in range(len(L[t])):
                    temp[i].append(L[t][j])
                    temp[i].append(t)
                 
        #print("temp  : ",temp)
        M = temp
        #print(M[:3][:3])
    #print(M[:3][:3])
    maxt = 0
    for ii in range(len(M)):
        if maxt < len(M[ii]) :
            maxt = len(M[ii])
    #print(maxt)
    ##print(M)
    #print(len(M))
    for ii in range(len(M)):
        for jj in range(len(M[ii]),maxt):
            M[ii].append(0)

    #print(M)
    if flag == 1:
        m = n
    n = maxt
if flag !=10:
    print(count)