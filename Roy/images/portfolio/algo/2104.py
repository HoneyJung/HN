import sys
N = int(input())
M = [int(x) for x in sys.stdin.readline().split()]
#print(M)
L = [0] # 합
L.append((0,N,sum(M),min(M)))
a = 1
flag = 0
while(1):
    for i in L[a:]:
        s,e,trash1,trash2 = i
        #print(s,e)
        if e - s <= 1:
            #print("hi")
            flag = 1
            break
        L.append((s,(s+e)//2,sum(M[s:(s+e)//2]),min(M[s:(s+e)//2])))
        L.append(((s+e)//2,e,sum(M[(s+e)//2:e]),min(M[(s+e)//2:e])))
    a = a * 2
    #print(L)
    #print(flag)
    #flag = 1
    if flag == 1:
        break
print(L)