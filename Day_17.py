#Shortest Path in a Graph
import heapq

n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [float('inf')] * (n+1)
dist[s] = 0
pq = [(0, s)]

while pq:
    d, node = heapq.heappop(pq)
    if d > dist[node]:
        continue
    for nei, w in graph[node]:
        if dist[nei] > d + w:
            dist[nei] = d + w
            heapq.heappush(pq, (dist[nei], nei))

print(dist[t] if dist[t] != float('inf') else -1)
