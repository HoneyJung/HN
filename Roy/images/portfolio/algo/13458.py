import sys
import collections
import copy
import itertools
N = int(input())
A = [int(x) for x in sys.stdin.readline().split()]
(B),(C) = sys.stdin.readline().split()
B = int(B)
C = int(C)
total = N 
#print("B,C",B,C)
for i in range(N):
    if A[i] >= B:
        A[i] = A[i] - B
    else:
        A[i] = 0
#print(A)
for i in range(N):
    if A[i] == 0 :
        continue
    elif int(A[i] / C) < A[i] / C:
        total = total + int(A[i] / C) + 1
        #print(int(A[i] / C) + 1)
    else:
        total = total + int(A[i] / C)
        #print(int(A[i] / C))
print(total)
    