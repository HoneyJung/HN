import sys
import collections
import heapq
#import copy

N = int(input())
Map = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
Map2 = [[0 for _ in range(N)] for _ in range(N)]

h = []
#deq = collections.deque([])
dx = [-1,0,0,1]
dy = [0,-1,1,0]

for i in range(N):
    for j in range(N):
        if Map[i][j] == 9:
            Map[i][j] = 0
            print("start : ", i,j)
            heapq.heappush(h,(0,i,j,2))
            #deq.append((i,j,2,0)) # 시작 위치, 크기 ,time

flag = -1 
time_stemp = 0
temp_count = 0
eatsomething=0
while h: # M N
    time,x,y,size = heapq.heappop(h)
    #x,y,size,time = deq.popleft()
    print(x,y,size,time)
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if xx >= N or xx < 0 or yy >= N or yy < 0 or Map2[xx][yy] == 1: # out of map or already visited in the loop
            flag = 1
            continue
        elif Map[xx][yy] < size and Map[xx][yy] != 0: # if can eat, restart there
            flag = 2
            if eatsomething == 0:
                eatsomething = eatsomething + 1 
            Map[xx][yy] = 0
            temp_count = temp_count + 1
            break
        elif (size - Map[xx][yy] == 0) or Map[xx][yy] == 0: # same size or empty -> deq.append
            flag = 3
            Map2[xx][yy] = 1
            heapq.heappush(h,(time+1,xx,yy,size))
            #deq.append((xx,yy,size,time+1))
            continue

        else: # bigger than shark? pass
            flag = 4 
            continue
        

    if flag == 2: # if you eat something, eat and restart
        h = []
        time_stemp = time + 1
        if temp_count == size:
            temp_count = 0
            size = size + 1
        Map2 = [[0 for _ in range(N)] for _ in range(N)]
        print((xx,yy,size,time))
        heapq.heappush(h,(time+1,xx,yy,size))
 
su = 0
print(size)
for i in range(2,int(size)):
    su = su + i
if eatsomething == 0:
    print(0)
else:
    print("answer : ", time_stemp)
    #print(time_stemp)