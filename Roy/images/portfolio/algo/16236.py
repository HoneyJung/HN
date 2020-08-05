import sys
import collections
import copy
import itertools

N = int(input())
Map = [[int(x) for x in sys.stdin.readline().split()]for _ in range(N)]
vst = [[0]*N for _ in range(N)]
deq = collections.deque([])
dx = [-1,0,0,1]
dy = [0,-1,1,0]
Lst = []
for i in range(N):
    for j in range(N):
        if Map[i][j] == 9:
            deq.append((i,j,2)) # x,y, size, depth
            vst[i][j] = 0
            Map[i][j] = 0
# bfs로 먹을 수 있는거 찾는다.
# 먹는다.

count = 0
print(deq)
flag  = 0
while deq:
    x,y,size = deq.popleft()
    #print("x,y,size ",x,y,size) 
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0 <= xx <N and 0<= yy < N:
            if vst[xx][yy] != 0 or Map[xx][yy] > size: # 큰거 있거나 이미 들렸으면.
                continue
            elif Map[xx][yy] != 0 and Map[xx][yy] < size: # 먹을 수 있는 거를 만났다면!?
                print("eat : ",xx,yy)
                if flag ==0:
                    flag = 1
                    xxx = xx
                    yyy = yy
                    xy = vst[x][y]+1
                else:
                    if xxx > xx:
                        xxx = xx
                        yyy = yy
                        xy = vst[x][y] + 1
                    elif xxx==xx and yyy>yy:
                        xxx = xx
                        yyy = yy
                        xy = vst[x][y] + 1
            else:
                deq.append((xx,yy,size))
                vst[xx][yy] = vst[x][y] + 1
    if not deq and flag == 1:                   
        count = count + 1
        if count == size:
            count = 0
            size = size+1
            deq = collections.deque([])
            vst = [[0]*N for _ in range(N)]
            vst[xx][yy] = xy
            Map[xx][yy] = 0
            deq.append((xx,yy,size))
            flag = 0
                    
print(Map)
print(xy)
