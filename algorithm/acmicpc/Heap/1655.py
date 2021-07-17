import sys
import heapq

max_heap = []
min_heap = []

ans = []

for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())

    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-x, x))
    else:
        heapq.heappush(min_heap, (x, x))

    if min_heap and max_heap[0][1] > min_heap[0][1]:
        temp_min = heapq.heappop(min_heap)[1]
        temp_max = heapq.heappop(max_heap)[1]
        heapq.heappush(max_heap, (-temp_min, temp_min))
        heapq.heappush(min_heap, (temp_max, temp_max))

    ans.append(max_heap[0][1])

for i in ans:
    print(i)
