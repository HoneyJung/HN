import sys
import collections
a,b = map(int,sys.stdin.readline().split())
time = 0
vis = [0 for _ in range(1000001)]
L = collections.deque([])
L.append([a,time])
flag = 0
while L:
    loc,t = L.popleft()
    # if loc <= 4:
    #print(loc,t)
    for i in range(3):
        if i == 0:
            temploc = loc + 1
        elif i == 1:
            temploc = loc - 1 
        elif i == 2:
            temploc = loc * 2
        if temploc == b:
            flag = 1
            break
        if 0 <= temploc and temploc <= 1000000:
            #print("후보 : ",temploc)
            if vis[temploc] == 0:
                L.append([temploc,t+1])
                vis[temploc] = 1
    if flag == 1:
        break
if a==b:
    print(0)
else:
    print(t+1)

