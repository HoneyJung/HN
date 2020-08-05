import heapq

a = []
heapq.heappush(a,(1,1,1))
heapq.heappush(a,(1,2,1))
heapq.heappush(a,(1,-1,1))
print(heapq.heappop(a))


