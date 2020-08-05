import sys
tc = int(input())

def turnright(m):
    templ = list(zip(*m))    
    for i in range(3):
        templ[i] = list(templ[i])
    for j in range(3):
        temp = templ[j][0]
        templ[j][0] = templ[j][2]
        templ[j][2] = temp
    m = templ
    return m
def turnleft(m):
    #print("hi",m)
    templ = list(zip(*m))
    for i in range(3):
        templ[i] = list(templ[i])
    #print("next :",templ)
    for j in range(3):
        temp = templ[0][j]
        templ[0][j] = templ[2][j]
        templ[2][j] = temp
    m = templ
    #print("hi",m)
    return m
def turnright2(a,b,c,d):
    temp = a[:]
    a = d[:]
    d = c[:]
    c = b[:]
    b = temp[:]
    return [a,b,c,d]

def turnleft2(a,b,c,d):
    temp = a[:]
    a = b[:]
    b = c[:]
    c = d[:]
    d = temp[:]
    return [a,b,c,d]
def turnright3(a,b,c,d):
    #print("here")
    temp1 = list(zip(*b))
    temp2 = list(zip(*d))
    for i in range(3):
        temp1[i] = list(temp1[i])
        temp2[i] = list(temp2[i])
    temp = a[:]
    a = temp2[0][:]
    temp2[0] = c[:]
    c = temp1[0][:]
    temp2[0] = temp[:]
    b = list(zip(*temp1))
    d = list(zip(*temp2))
    for i in range(3):
        b[i] = list(b[i])
        d[i] = list(d[i])
    #print("3 : ",a,b,c,d )
    return  [a,b,c,d]
def turnleft3(a,b,c,d):
    temp1 = list(zip(*b))
    temp2 = list(zip(*d))
    for i in range(3):
        temp1[i] = list(temp1[i])
        temp2[i] = list(temp2[i])    
    temp = a[:]
    a = temp1[:]
    temp1 = c[:]
    c = temp2[:]
    temp2 = temp[:]
    b = list(zip(*temp1))
    d = list(zip(*temp2))
    for i in range(3):
        b[i] = list(b[i])
        d[i] = list(d[i])
    return [a,b,c,d]
def turnright4(a,b,c,d):
    temp1 = list(zip(*a))
    temp2 = list(zip(*b))
    temp3 = list(zip(*c))
    temp4 = list(zip(*d))    
    for i in range(3):
        temp1[i] = list(temp1[i])
        temp2[i] = list(temp2[i])
        temp3[i] = list(temp3[i])
        temp4[i] = list(temp4[i])
    temp = temp1[0][:]
    temp1[0] = temp4[0][:]
    temp4[0] = temp3[0][:]
    temp3[0] = temp2[0][:]
    temp2[0] = temp[:]
    a = list(zip(*temp1))
    b = list(zip(*temp2))
    c = list(zip(*temp3))
    d = list(zip(*temp4))
    for i in range(3):
        a[i] = list(a[i])
        b[i] = list(b[i])
        c[i] = list(c[i])
        d[i] = list(d[i])
    return [a,b,c,d]
def turnleft4(a,b,c,d,s): # 0213
    temp1 = list(zip(*a))
    temp2 = list(zip(*b))
    temp3 = list(zip(*c))
    temp4 = list(zip(*d))
    for i in range(3):
        temp1[i] = list(temp1[i])
        temp2[i] = list(temp2[i])
        temp3[i] = list(temp3[i])
        temp4[i] = list(temp4[i])
    temp = temp1[0][:]
    temp1[0] = temp2[0][:]
    temp2[0] = temp3[0][:]
    temp3[0] = temp4[0][:]
    temp4[0] = temp[:]
    a = list(zip(*temp1))
    b = list(zip(*temp2))
    c = list(zip(*temp3))
    d = list(zip(*temp4))
    for i in range(3):
        a[i] = list(a[i])
        b[i] = list(b[i])
        c[i] = list(c[i])
        d[i] = list(d[i])
    return [a,b,c,d]
for _ in range(tc):
    N = int(input())
    M = []
    M.append([['w','w','w'],['w','w','w'],['w','w','w']]) # U 0
    M.append([['y','y','y'],['y','y','y'],['y','y','y']]) # D 1
    M.append([['r','r','r'],['r','r','r'],['r','r','r']]) # F 2 
    M.append([['o','o','o'],['o','o','o'],['o','o','o']]) # B 3 
    M.append([['g','g','g'],['g','g','g'],['g','g','g']]) # L 4 
    M.append([['b','b','b'],['b','b','b'],['b','b','b']]) # R 5
    put = sys.stdin.readline().split()
    for i in range(N):
        s,w = put[i][0],put[i][1]
        #print(s,w)
        if s=='U':
            if w == '+':
                M[0] = turnright(M[0])
                M[2][0],M[5][0],M[3][0],M[4][0] = turnright2(M[2][0],M[5][0],M[3][0],M[4][0])
            else:
                M[0] = turnleft(M[0])
                M[2][0],M[5][0],M[3][0],M[4][0] = turnleft2(M[2][0],M[5][0],M[3][0],M[4][0])
        if s=='D':
            if w == '+':
                M[1] = turnright(M[1])
                M[2][2],M[5][2],M[3][2],M[4][2] = turnright2(M[2][2],M[5][2],M[3][2],M[4][2])
            else:
                M[1] = turnleft(M[1])
                M[2][2],M[5][2],M[3][2],M[4][2] = turnleft2(M[2][2],M[5][2],M[3][2],M[4][2])
        if s=='F':
            if w == '+':
                #print(M[4])
                M[2] = turnright(M[2])
                M[0][2],M[5],M[1][0],M[4] =turnright3(M[0][2],M[5],M[1][0],M[4],s)
            else:
                M[2] = turnleft(M[2])
                M[0][2],M[5],M[1][0],M[4] = turnleft3(M[0][2],M[5],M[1][0],M[4],s)
        if s=='B':
            if w == '+':
                M[3] = turnright(M[3])
                M[0][0],M[4],M[1][0],M[5] = turnright3(M[0][0],M[4],M[1][0],M[5],s)
            else:
                turnleft(M[3])
                M[0][0],M[4],M[1][0],M[5] = turnleft3(M[0][0],M[4],M[1][0],M[5],s)
        if s=='L':
            if w == '+':
                M[4] = turnright(M[4])
                M[0],M[2],M[1],M[3] = turnright4(M[0],M[2],M[1],M[3],s)
            else:
                M[4] = turnleft(M[4])
                M[0],M[2],M[1],M[3] = turnleft4(M[0],M[2],M[1],M[3],s)
        if s=='R':
            if w == '+':
                M[5] = turnright(M[5])
                M[0],M[3],M[1],M[2] = turnright4(M[0],M[3],M[1],M[2],s)
            else:
                M[5] = turnleft(M[5])
                M[0],M[3],M[1],M[2] =turnleft4(M[0],M[3],M[1],M[2],s)
        print("finish")
        print(M)
    #print(tempa)