import sys
import collections
import copy
N,M = map(int,sys.stdin.readline().split())
Map = [[int(x) for x in sys.stdin.readline().strip()] for _ in range(N)]
deq = collections.deque([])

vst = [[0] * M for _ in range(N)]
#print (vst)
vst = [[[0,0] for _ in range(M)] for _ in range(N)]
#print(vst)

#vst= [[[0]*2 for j in range(M)] for i in range(N)]
vst[0][0][0] = 1
#print (vst)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
deq.append((0,0,0))
while deq:
    p,q,c = deq.popleft()
    for i in range(4):
        a = p+dx[i]
        b = q+dy[i]
        if 0<=a<N and 0<=b<M : ### map 안일때만
            if Map[a][b] == 1 and c ==0 and vst[a][b][1] == 0:  ############################# 벽이고 벽 안뚫어봤고 가본곳 아니라면.
                vst[a][b][1] = vst[p][q][0] + 1
                deq.append((a,b,1))
            if Map[a][b] == 0 and vst[a][b][c] == 0:
                vst[a][b][c] = vst[p][q][c] + 1
                deq.append((a,b,c))
#print(vst)
if vst[N-1][M-1][0] == 0 and vst[N-1][M-1][1] == 0:
    print("-1")
else:
    if vst[N-1][M-1][0] == 0 or vst[N-1][M-1][1] == 0:
        print(max(vst[N-1][M-1][0],vst[N-1][M-1][1]))
    else:
        print(min(vst[N-1][M-1][0],vst[N-1][M-1][1]))
                
    