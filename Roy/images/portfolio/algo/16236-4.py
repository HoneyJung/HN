import sys
import collections
import heapq

N = int(input())
Map = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)] # 전체 지도
Map2 = [[0 for _ in range(N)] for _ in range(N)] # visited map

h = []
dx = [-1,0,0,1]
dy = [0,-1,1,0]
#########################################################돌면서 상어위치 찾고 heap에 push
#33##############33 heap 우선순위는 시간(0에서부터 시작) -> y축 -> x축 (가장 가까운거 중 젤 위, 젤 왼쪽에 있는걸 먹어야하기 때무네에ㅔ))


for i in range(N):
    for j in range(N):
        if Map[i][j] == 9:
            Map[i][j] = 0
            Map2[i][j] = 1 
            #print("start : ", i,j)
            heapq.heappush(h,(0,i,j,2)) # 시간, 위치, 크기
#################################################################################


count = 0 ########3 먹은거 개수 저장하기 위한 변수 -> 상어의 성장을 위해
time_stemp = 0 ############마지막 먹은 시간을 저장하기 위한 변수
while h: # bfs
    time,i,j,size = heapq.heappop(h)
    #print(time,i,j,size)
    if size > Map[i][j] and Map[i][j] != 0: ########### eat!!!!!!!!!!!!11
        #print("eat")
        time_stemp = time
        #print((time,i,j,size))
        Map[i][j] = 0
        Map2 = [[0 for _ in range(N)] for _ in range(N)] # initialize visited map
        while h: # 먹었으면 heap 다 빼고 먹은거만 넣고 다시 bfs
            heapq.heappop(h)
        count = count + 1

        if count == size: # 자신의 몸 크기 만큼 먹으면 사이즈 커짐
            count = 0
            size = size + 1
        
        heapq.heappush(h,(time,i,j,size))
        continue


    for k in range(4): # try 
        ii,jj = i+dx[k],j+dy[k]
        if ii >= N or ii < 0 or jj >= N or jj < 0 : # out of map
            continue
        elif size < Map[ii][jj] or Map2[ii][jj]==1: # bigger size or already visited
            Map2[ii][jj] = 1
            continue
        elif size == Map[ii][jj] or Map[ii][jj] == 0: # same size
            Map2[ii][jj] = 1
            heapq.heappush(h,(time+1,ii,jj,size))
            #print((time+1,ii,jj,size))
        else: # can eat? 일단 먹지 않고 힙에 넣어야한다. 4번째 예시 input에서 (0,2)를 먹고 (1,1)이 아닌 (0,4)를 먹어야 하기 때문에
            heapq.heappush(h,(time+1,ii,jj,size))
            #print((time+1,ii,jj,size))

            continue

print(time_stemp)
