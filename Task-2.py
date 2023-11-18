f1 = open('input-2.txt', 'r')
f2 = open('output-2.txt', 'w')

n, m = map(int,f1.readline().split(' '))
lst = [[] for j in range(n+1)]
for row in range(m):
    v,e= map(int,f1.readline().strip().split())
    lst[v].append(e)

def bfs(lst, start):
    queue = [start]
    visited = [False] * (len(lst))
    visited[start] = True
    order = []

    while queue:
        current_node = queue.pop(0)
        order.append(current_node)
        for children in lst[current_node]:
            if not visited[children]:
                visited[children] = True
                queue.append(children)

    return order

result = bfs(lst, 1)
for i in result:
    f2.write(f'{i} ')
    print(i,end=' ')

