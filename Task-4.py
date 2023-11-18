f1 = open('input-4.txt', 'r')
f2 = open('output-4.txt', 'w')
n, m = map(int,f1.readline().strip('\n').split(' '))
graph = {}
for i in range(1, n + 1):
    graph[i] = []

for j in range(m):
    a, b = map(int,f1.readline().strip('\n').split(' '))
    graph[a].append(b)
def isCycle(graph):
    def dfs(node):
        if node in visited:
            return False
        visited.add(node)
        recursion_stack.add(node)

        for children in graph.get(node, []):
            if children in recursion_stack or dfs(children):
                return True

        recursion_stack.remove(node)
        return False
    visited = set()
    recursion_stack = set()

    # check for all nodes
    for node in graph:
        if dfs(node):
            return True

    return False
var = isCycle(graph)
if var == True:
    f2.write('Yes')
    print('Yes')
else:
    f2.write('No')
    print('No')

f1.close()
f2.close()