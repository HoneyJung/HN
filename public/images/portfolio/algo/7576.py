import sys
import collections
##################################################################################33
'''
일단 한바꾸 돌면서 1의 위치를 찾아 stack에 넣어준다. phase라는 것도 같이 넣어준다.
phase라는 것은 몇번째 턴이 진행되고 있는지(해당 감염이 몇번 째 unit time에 진행되는지)를 기록해주는 변수.
첫바꾸 1의 위치를 찾을 때는 당연히 phase = 0
그리고 첫바꾸 돌 떄, 0의 수를 count 해준다. (앞으로 다 전염시키기 위해 바꿔야할 토마토 개수)
 
 1) 일단 count = 0 이면 0이 없다는 거니까 0출력 후 종료
 2) count 0보다 크면 stack에서 하나씩 끄집어 오면서 상하좌우 체크해주고 0인거 있으면 push. 도중에 count = 0  되면 breakㅌ
    젤 마지막에 push한 놈의 phase 출력.
 3)count 가 0이 되기 전에 stack이 비어버리면 다 전염 못 시켰는데 더 이상 나아갈 곳이 없다는 뜻. -> -1

'''
#####################################################################################
M,N = map(int,sys.stdin.readline().split())
ary = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
#print(ary)
count = N*M ###############앞으로 전염시켜야할 토마토 수.
stack = collections.deque([]); #################이미 전염된거 (i,j,phase).
phase = 0 #########몇번째phase인지.
mx = [1,-1,0,0]
my = [0,0,1,-1]
c = 0
tmp = 0
for i in range(N):
    for j in range(M):
        if(ary[i][j] == 1):
            count = count - 1
            stack.append((i,j,phase))
        elif(ary[i][j] == -1):
            count = count - 1
#print("count",count)
#print(stack)

if(count==0):
    print("0")
while(count > 0):
    if not stack:
        print("-1")
        break             
    a,b,c = stack.popleft()
    for mv in range(4):#############주변꺼가
        if a + mx[mv] >= N or a + mx[mv] < 0 or b + my[mv] >= M or b + my[mv] < 0: ###############    ary 밖으로 벗어날때
            continue
        elif ary[a + mx[mv]][b+my[mv]] == 0:  ##################################### 안익은경우.
            stack.append((a+mx[mv],b+my[mv],c+1))  ############# stack에 넣어주고 phase는 original phase + 1
            ary[a + mx[mv]][b+my[mv]] = 1 ############# ary 값 바꿔주고
            count = count -1 ########전염시킬때마다 count--
#            print(stack)
            continue
    
if(count == 0 and c > 0):
    a,b,c = stack.pop()
    print(c)
            
        

