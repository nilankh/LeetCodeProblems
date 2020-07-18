#957
def prisonAfterNDays(cells, N):
        _map = {}
    
        for i in range(N):
            s = str(cells)
            if s in _map:
                loop_length = i - _map[s]
                remaining_days = (N - i) % loop_length
                return prisonAfterNDays(cells, remaining_days)
            else:
                _map[s] = i
                prev = cells[0]
                for j in range(1,7):
                    curr, next = cells[j], cells[j+1]
                    cells[j] = 1 - (prev ^ next) #!(prev ^ next)
                    prev = curr
            cells[0], cells[7] = 0,0
        
        return cells

arr = [int(x) for x in input().split()]
N = int(input())
print(prisonAfterNDays(arr,N))
def mulrec(m,n):
    if n==0:
        return 0
    return m+mulrec(m,n-1)       

m=int(input())
n=int(input())
print(mulrec(m,n))

    
g.bfs()
