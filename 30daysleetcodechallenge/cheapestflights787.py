import heapq
def cheapestFlights(n, flights, src, dest, k):
    adj = {u: [] for u in range(n)}
    for f in flights:
        adj[f[0]].append((f[1], f[2]))
    Q = []
    Q.append((0, src, k + 1))
    while len(Q) > 0:
        top = heapq.heappop(Q)
        d = top[0]
        u = top[1]
        e = top[2]
        if dest == u: return d
        if e > 0:
            for v in adj[u]:
                heapq.heappush(Q, (d + v[1], v[0], e - 1))

    return -1

n = int(input())
flights = []
for i in range(0, n):
    arr = [int(x) for x in input().split()]
    flights.append(arr)
src = int(input())
dest = int(input())
k = int(input())
j = cheapestFlights(n, flights, src, dest, k)
print(j)
