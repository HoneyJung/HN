import sys
import collections
import copy
import itertools
N = int(input())
number = [int(x) for x in sys.stdin.readline().split()]
deq = []
deq1 = collections.deque([])
a,b,c,d = sys.stdin.readline().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
#print("eiofnoiqnfoiqenfoineqoifnqeoifn")
for i in range(a):
    deq.append(0)
for i in range(b):
    deq.append(1)
for i in range(c):
    deq.append(2)
for i in range(d):
    deq.append(3)
deq = (itertools.permutations(deq))
#print("deq : ",type(deq))
Min = sys.maxsize
Max = -sys.maxsize

for x in deq:
    i = 0
    total = number[i]
    i = i + 1 
    #x = deq.pop(0)
    #x = list(x)
    for j in x:
        if j ==0:
            total = total + number[i]
        elif j ==1:
            total = total - number[i]
        elif j ==2:
            total = total * number[i]
        elif j ==3:
            if total < 0:
                total = total*(-1)
                total = total / number[i]
                total = int(total) * (-1)
            else:
                total = total / number[i]
                total = int(total)
        i = i+1

    if Min > total:
        Min = total
    if Max <total:
        Max = total
print(Max)
print(Min)