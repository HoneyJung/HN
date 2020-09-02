import sys
#import pprint
import collections
N = int(input())
r,c = map(int,sys.stdin.readline().split())
print(r,c)
Q = collections.deque([])
Map  = [[x for x in list(sys.stdin.readline())] for _ in range(r)]
mx = [[0,1],[0,-1],[1,0],[-1,0]]
my = [[0,1],[0,-1],[1,0],[-1,0]]
print(Map)
# 수감자 위치
for i in range(r):
    for j in range(c):
        print(i,j)
        if Map[i][j] == '$':
            Q.append((i,j))

print(Q)
while Q:
    a,b = Q.popleft()
