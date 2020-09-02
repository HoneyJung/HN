import sys
N,K = map(int,sys.stdin.readline().split())
L = []

for i in range(N):
    a = int(input())
    L.append(a)
L2 = L[:K]
L2.sort()
S = L2[(K+1)//2-1]
idx = K
#print(L)
#print(L2)
idx2 = 0
if K==N:
    print(L2[(K+1)//2-1])
else:
    while 1:
        #print(L2[(K+1)//2-1])
        L2.remove(L[idx2])
        flag = 0 
        for i in range(K-1):
            #print(idx,i)
            if L[idx] <= L2[i]:
                #print(idx,i)
                flag = 1
                break
        if flag == 0:
            i = i + 1
        #print(i)
        L2.insert(i,L[idx])
        #print(L)
        idx = idx + 1
        idx2 = idx2 + 1
        #print(idx)
        S = S + L2[(K+1)//2-1]
        #print(L2)
        #print(L2[(K+1)//2-1])
        if idx == len(L):
            break
    print(S)