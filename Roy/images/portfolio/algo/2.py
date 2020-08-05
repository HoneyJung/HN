import sys
tc = int(input())
for _ in range(tc):
    m,n = map(int,sys.stdin.readline().split())
    M = [[int(x) for x in sys.stdin.readline().split()] for _ in range(m)]
    #print(M)
    flag = 0
    for i in range(m):
        for j in range(n):
            if M[i][j] == 1:
                if i-2 >=0 and M[i-2][j] == 1:
                    print("NO")
                    flag = 1
                    break        
                if i+2 < m and M[i+2][j] == 1:
                    print("NO")
                    flag = 1
                    break
                        
                if j-2 >= 0 and M[i][j-2] == 1:
                    print("NO")
                    flag = 1
                    break
                        
                if j+2 < n and M[i][j+2] == 1:
                    print("NO")
                    flag = 1
                    break
        if flag ==1:
            break
    if flag == 0:
        print("YES")
                