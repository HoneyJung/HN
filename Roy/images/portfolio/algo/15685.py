import sys
import collections
N = int(input())
Map = [[0 for _ in range(101)] for _ in range(101)]
#Map2 = [[0 for _ in range(100)] for _ in range(99)]
target = [(1,0), (0,-1), (-1,0), (0,1)]


for _ in range(N):
    Q = []
    QQ = []
    #Q = collections.deque([])
    #QQ = collections.deque([])
    x,y,d,g = map(int,sys.stdin.readline().split())
    if g == 0:
        QQ.append(d)
        #print("ei")
    else:
        end = (x + target[d][0], y + target[d][1])
        Q.append(d)
        QQ = Q[:]
        count = 0
        while(Q):
            p = Q.pop()
            if p == 0:
                pp = 1
            if p == 1:
                pp = 2
            if p == 2:
                pp = 3
            if p == 3:
                pp = 0
            QQ.append(pp)
            if len(Q)==0: # 다 뺏으면 새로운 큐로 교체
                #print(Q,QQ)
                if count == g-1:
                    break
                count = count + 1 
                Q = QQ[:]
    
    for i in QQ:    
        Map[x][y] = 1
        x = x + target[i][0]
        y = y + target[i][1]
    Map[x][y] = 1 

answer = 0
for i in range(100):
    for j in range(100):
        temp = 0
        if Map[i][j] == 1:
            temp = temp + 1
        if Map[i][j+1] == 1:
            temp = temp + 1
        if Map[i+1][j] == 1:
            temp = temp + 1
        if Map[i+1][j+1] == 1:
            temp = temp + 1
        if temp == 4:
            answer = answer + 1 
print(answer)
