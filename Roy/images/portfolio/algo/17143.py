
import sys

R,C,S = map(int, sys.stdin.readline().split())
M = [[[] for _ in range(C)] for _ in range(R)]
L = []
dx = [0,-1,1,0,0]
dy = [0,0,0,1,-1]
for i in range(S):
    r,c,s,d,z = map(int,sys.stdin.readline().split())
    r= r-1
    c=c-1
    L.append([r,c,s,d,z])
    M[r][c].append([s,d,z])

count = 0
for i in range(C):
    #print("turn")
    #print(M)
    for j in range(R):
        if len(M[j][i]) != 0: # 낚시꾼 사냥
            count = count + M[j][i][0][2]
            #print(L)
            #print([j,i,M[j][i][0][0],M[j][i][0][1],M[j][i][0][2]])
            L.remove([j,i,M[j][i][0][0],M[j][i][0][1],M[j][i][0][2]])
            M[j][i] = []
            #print("kill")
            break
    #print(M)
    #print(L)
    for j in range(len(L)): # move
        r,c,s,d,z = L[j]
        #print(L[j])
        ogr,ogc,ogs,ogd,ogz = L[j]
        for t in range(s):
            r = r + dx[d]
            c = c + dy[d]
            if r == R:
                d = 1
                r = r - 2
            elif r == -1:
                d = 2
                r = r + 2
            elif c == C:
                d = 4
                c = c - 2
            elif c == -1:
                d = 3
                c = c + 2
            #print(r,c,d)
        M[ogr][ogc].pop(0)
        M[r][c].append([s,d,z])
        L[j][0] = r
        L[j][1] = c
        L[j][3] = d
    #print(M)
    for m1 in range(R): ### eat
        for m2 in range(C):
            if len(M[m1][m2]) >= 2:
                #print("eat")
                #print(M[m1][m2])
                Max = 0
                #Maxidx = 0                
                for m3 in range(len(M[m1][m2])):
                    if Max < M[m1][m2][m3][2]:
                        Max = M[m1][m2][m3][2]
                        maxidx = m3
                #print(maxidx)
                for m3 in range(len(M[m1][m2])):
                    if m3 == maxidx:
                        continue
                    L.remove([m1,m2,M[m1][m2][m3][0],M[m1][m2][m3][1],M[m1][m2][m3][2]])
                M[m1][m2] = [[M[m1][m2][maxidx][0],M[m1][m2][maxidx][1],M[m1][m2][maxidx][2]]]
                #print(M[m1][m2])
    #print(M)

print(count)