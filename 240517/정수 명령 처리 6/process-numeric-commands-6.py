import heapq

class PQ:
    def __init__(self):
        self.items = []
    def push(self, item):
        heapq.heappush(self.items, -item)
    def empty(self):
        # if not self.items:
        #     return 1
        # else:
        #     return 0
        return not self.items
    def size(self):
        return len(self.items)
    def pop(self):
        if self.empty():
            raise Exception("empty")
        return -heapq.heappop(self.items)
    def top(self): 
        if self.empty():
            raise Exception("PriorityQueue is empty")
                        
        return -self.items[0]

n = int(input())

pq = PQ()
for _ in range(n):
    arr = input().split()
    if arr[0] == "push":
        pq.push(int(arr[1]))
    if arr[0] == "size":
        print(pq.size())
    if arr[0] == "empty":
        print(int(pq.empty()))
    if arr[0] == "pop":
        print(pq.pop())
    if arr[0] == "top":
        print(pq.top())