def shortest_path(graph, s, d):
    q = [(s, [s])]
    visited = set()

    while q:
        node, path = q.pop(0)
        visited.add(node)

        if node == d:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append((neighbor, path + [neighbor]))

    return None


f1 = open('input-5.txt', 'r')
f2 = open('output-5.txt', 'w')

N, M, des = map(int, f1.readline().split())

# creating dictonary for adj list
G = {}
for i in range(N + 1):
    G[i] = []

for i in range(M):
    s, d = map(int, f1.readline().split())
    G[s].append((d))
    G[d].append((s))  # undir

path = shortest_path(G, 1, des)

print(f'Time: {len(path) - 1} \nShortest Path: {str(path).strip("[]").replace(",", "")}', file=f2)

f1.close()
f2.close()
