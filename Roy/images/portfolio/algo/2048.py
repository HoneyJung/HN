import sys
import collections
import copy
N = int(input())
Map = [[int(x) for x in sys.stdin.readline().split()]  for _ in range(N)]
#print (Map)
deq = collections.deque([])
qu = collections.deque([])
deq.append((Map,0))
'''
방향별 함수.
한 줄에서 0이 아닌거 queue에 넣고 순서대로 넣어줌. 안같아야 순서 ++  해줌. 같으면 합치고 ++
'''
def move(dr,A):
    if dr == 0:### <-------
        for i in range(N):
            for j in range(N):
                if A[i][j] != 0: ################# 한줄 0이 아닌거 push
                    qu.append(A[i][j])
                    A[i][j] =0
            flag = 0
            j=0
            while qu:
                x = qu.popleft()
                if A[i][j] == 0:
                    A[i][j] = x
                    continue
                if A[i][j] == x and flag ==0 : ## 같으면서 바뀐적 없는것이면!?
                    A[i][j] = A[i][j] * 2
                    flag = 1
                    continue
                if flag == 1 or A[i][j] != x: # 바뀐적 있거나 같지 않으면
                    j = j + 1
                    flag = 0
                    A[i][j] = x
    if dr == 1: #----------->
        for i in range(N):
            for j in range(N-1,-1,-1):
                if A[i][j] != 0: ################# 한줄 0이 아닌거 push
                    qu.append(A[i][j])
                    A[i][j] =0
            flag = 0
            j=N-1
            while qu:
                x = qu.popleft()
                if A[i][j] == 0:
                    A[i][j] = x
                    continue
                if A[i][j] == x and flag ==0 : ## 같으면서 바뀐적 없는것이면!?
                    A[i][j] = A[i][j] * 2
                    flag = 1
                    continue
                if flag == 1 or A[i][j] != x: # 바뀐적 있거나 같지 않으면
                    j = j -1
                    flag = 0
                    A[i][j] = x    
    if dr == 2: # up
        for j in range(N):
            for i in range(N):
                if A[i][j] != 0: ################# 한줄 0이 아닌거 push
                    qu.append(A[i][j])
                    A[i][j] =0
            flag = 0
            i=0
            while qu:
                x = qu.popleft()
                if A[i][j] == 0:
                    A[i][j] = x
                    continue
                if A[i][j] == x and flag ==0 : ## 같으면서 바뀐적 없는것이면!?
                    A[i][j] = A[i][j] * 2
                    flag = 1
                    continue
                if flag == 1 or A[i][j] != x: # 바뀐적 있거나 같지 않으면
                    i = i + 1
                    flag = 0
                    A[i][j] = x
    if dr == 3: # down
        for j in range(N):
            for i in range(N-1,-1,-1):
                if A[i][j] != 0: ################# 한줄 0이 아닌거 push
                    qu.append(A[i][j])
                    A[i][j] =0
            flag = 0
            i=N-1
            while qu:
                x = qu.popleft()
                if A[i][j] == 0:
                    A[i][j] = x
                    continue
                if A[i][j] == x and flag ==0 : ## 같으면서 바뀐적 없는것이면!?
                    A[i][j] = A[i][j] * 2
                    flag = 1
                    continue
                if flag == 1 or A[i][j] != x: # 바뀐적 있거나 같지 않으면
                    i = i -1 
                    flag = 0
                    A[i][j] = x 
    Max = -1  
    for i in range(N):
        if Max < max(A[i]) :
            Max = max(A[i])
    return Max
'''
ap = copy.deepcopy(Map)
move(0,ap)
print(ap)
ap = copy.deepcopy(Map)              
move(1,ap)
print(ap)              
ap = copy.deepcopy(Map)
move(2,ap)
print(ap) 
ap = copy.deepcopy(Map)             
move(3,ap)
print(ap)              
'''
'''
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0 
64 64 128 0 0 0 0 0 0 0
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0 
64 64 128 0 0 0 0 0 0 0
128 32 2 4 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0

10
8 8 4 16 32 0 0 8 8 8
8 8 4 0 0 8 0 0 0 0
16 0 0 16 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 16
0 0 0 0 0 0 0 0 0 2
'''

#move(3)
#print(Map)              
Max = -1  
for i in range(N):
    if Max < max(Map[i]) :
        Max = max(Map[i])
#print(Max)
while deq:
    temp,depth = deq.popleft() #### BFS
    if depth == 5:
        break
     
    for dr in range(4):
        A = copy.deepcopy(temp)
        re = move(dr,A) ### A를 변경해준다.
        if Max < re:
            Max = re 
        deq.append((A,depth+1))
print(Max)

