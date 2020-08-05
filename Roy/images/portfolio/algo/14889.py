import sys
import collections
import copy
import itertools
N = int(input())
Map = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
#print(Map)
n = N/2
A = [[x] for x in range(N)]
deq = collections.deque([])


def combi(deq2):
    deq1 = collections.deque([])
    while deq2:
        a = deq2.popleft()
        b = a.pop()
        a.append(b)
        for i in range(b+1,N):
            deq1.append(a+[i])
    return deq1
################################################33#3 조합 계산
for i in range(N):
    deq.append(A[i])
for i in range(int(n)-1):
    deq = combi(deq)
####################################################3
'''
items = []
for i in range(N):
    items.append(i)
K = (list(itertools.combinations(items,int(N/2))))

'''
result = 0
Min = -1
while deq:
    t0=0
    t1=0
    x = deq.popleft()
    for i in range(N):
        if i not in x: ############ 반대편 
            for j in range(N):
                if j not in x: 
                    t1 = t1 + Map[i][j]
        else:
            for j in range(N):
                if j in x:
                    t0 = t0 + Map[i][j]
                    
    result = t0 - t1
    if result < 0:
        result = result * (-1)
    if Min > result or Min < 0:
        Min = result
    #print(t0,t1)
print(Min)
