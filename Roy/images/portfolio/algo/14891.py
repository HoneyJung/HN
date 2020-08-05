import sys
import collections
import copy
Map = [[int(x) for x in sys.stdin.readline().strip()] for _ in range(4)]
N = int(input())
#print(Map)
#print(N)
deq = collections.deque([])
stack = collections.deque([])
def rot(k,F): ## 회전시키는 함수.
    if F==1: ## 시계방향
        temp = Map[k].pop()
        Map[k].insert(0,temp)
    else:
        temp = Map[k].pop(0)
        Map[k].append(temp)
'''
rot(0,1)
rot(0,-1)
print(Map)
'''
for _ in range(N):
    M,flag = map(int,sys.stdin.readline().split())
    #print(M,flag)
    deq.append((M,flag)) # 시작점 넣고
    visit = [0]*4
    while deq:
        M,flag = deq.popleft()
        M = M - 1
        visit[M] = 1
        stack.append((M,flag)) 
        # print("M,flag",M,flag)
        if 0<=M-1<4 and visit[M-1] == 0: ### 왼쪽꺼
            if Map[M][6] + Map[M-1][2] == 1: ############ 왼쪽꺼 극이 다르면
        #        print("left rot")
                #rot(M-1,flag*(-1))
                deq.append((M,flag*(-1)))
        if 0<=M+1<4 and visit[M+1] == 0:
            if Map[M][2] + Map[M+1][6] == 1: ############ 오른쪽꺼 극이 다르면
                #print(Map[M][2],Map[M+1][7])
        #        print("right rot")
                #rot(M+1,flag*(-1))
                deq.append((M+2,flag*(-1)))
        #rot(M,flag)##일단 그거는 돌리고
    #print("finish phase")
    while stack:
        M,flag = stack.popleft()
        rot(M,flag)
    
    #print(Map)



score = 0
if Map[0][0] == 1:
    score = score + 1 
if Map[1][0] == 1:
    score = score + 2   
if Map[2][0] == 1:
    score = score + 4
if Map[3][0] == 1:
    score = score + 8
print(score) 