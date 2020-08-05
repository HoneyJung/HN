import sys
inputString = sys.stdin.readline()
inputString = inputString[:len(inputString)-1]
#print(inputString)
L = [0,0,0,0]
Count = [0,0,0,0]
flag = 0
for i in range(len(inputString)):
    if inputString[i] == '(':
        L[0]  = L[0] + 1
    elif inputString[i] == ')':
        L[0]  = L[0] - 1
        Count[0] = Count[0] + 1
    elif inputString[i] == '{':
        L[1]  = L[1] + 1
    elif inputString[i] == '}':
        L[1]  = L[1] - 1
        Count[1] = Count[1] + 1
    elif inputString[i] == '[':
        L[2]  = L[2] + 1
    elif inputString[i] == ']':
        L[2]  = L[2] - 1
        Count[2] = Count[2] + 1
    elif inputString[i] == '<':
        L[3]  = L[3] + 1
    elif inputString[i] == '>':
        L[3]  = L[3] - 1
        Count[3] = Count[3] + 1
    for j in range(4): # 괄호 잘못되었는지 확인
        if L[j] < 0:
            flag = 1
            break
    if flag == 1: #잘못됐으면
        break
for i in range(len(L)):
    if L[i] != 0:
        flag = 1
        break
if flag == 1:
    print(-1)
else:
    print(sum(Count))