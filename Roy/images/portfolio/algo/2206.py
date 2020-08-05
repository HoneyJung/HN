import sys
import collections
import copy
N,M = map(int,sys.stdin.readline().split())
Map = [[int(x) for x in sys.stdin.readline().strip()] for _ in range(N)]
deq = collections.deque([])
deq1 = collections.deque([])
#print(N,M,Map)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
vst = [[0]*M for _ in range(N)]
#vst1 = [[0]*M for _ in range(N)]
vst[0][0] = 1

s = collections.deque([])
def f(FF,vst2):
    #print(vst2)
    while deq:
        if FF == 1:
            #print(deq)
            a,b,c = deq.popleft()
            vst2[a][b] = c
        else:
            a,b = deq.popleft()
        
        if a==N-1 and b == M-1:
            return vst2[a][b]
        for i in range(4):
            if a+dx[i] < 0 or a+dx[i] >= N or b+dy[i] <0 or b+dy[i] >= M :
                continue
            if Map[a+dx[i]][b+dy[i]] == 1: ###############3 벽이면
                if FF == 0:
                    s.append((a+dx[i],b+dy[i]))
                    if vst2[a+dx[i]][b+dy[i]] == 0:
                        vst2[a+dx[i]][b+dy[i]] = vst2[a][b] + 1
                    else:     
                        vst2[a+dx[i]][b+dy[i]] = min(vst2[a+dx[i]][b+dy[i]] ,vst2[a][b] + 1)
                continue
            else:
                if vst2[a+dx[i]][b+dy[i]] != 0 and vst2[a+dx[i]][b+dy[i]] <= vst2[a][b]+1:
                    continue
                else:
                    if FF == 0:
                        deq.append((a+dx[i],b+dy[i]))
                    else:
                        deq.append((a+dx[i],b+dy[i],vst2[a][b]+1))
                    vst2[a+dx[i]][b+dy[i]] = vst2[a][b] + 1
    return vst2[N-1][M-1]
deq.append((0,0))
f(0,vst)
firstresult = vst[N-1][M-1]

while s:
    a,b = s.popleft()
    for i in range(4):
        if a+dx[i] < 0 or a+dx[i] >= N or b+dy[i] <0 or b+dy[i] >= M : # out of range
            continue
        if Map[a+dx[i]][b+dy[i]] == 1: ############### 또 벽이면!?
            continue
        elif firstresult ==0:
            if vst[a+dx[i]][b+dy[i]] != 0:
                continue
            deq1.append((a+dx[i],b+dy[i],vst[a][b] + 1))
        else:
            deq1.append((a+dx[i],b+dy[i],vst[a][b] + 1))

ma = vst[N-1][M-1]
print(vst)
print(deq1)
#print(deq)

while deq1:
    a,b,c = deq1.popleft()
    deq.append((a,b,c))
    vst = [[0]*M for _ in range(N)]
    vst[a][b] = c
    result = f(1,vst)
#    print(result)
    if (result < ma and result != 0) or ma == 0:
        ma = result

if ma == 0:
    print(ma-1)
else:
    print(ma)

#print(vst)
