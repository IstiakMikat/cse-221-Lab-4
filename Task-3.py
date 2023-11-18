f1 = open('input-3.txt', 'r')
f2 = open('output-3.txt', 'w')

n, m = map(int,f1.readline().split(' '))
lst = [[] for j in range(n+1)]
for row in range(m):
    v,e= map(int,f1.readline().strip().split())
    lst[v].append(e)
    lst[e].append(v)
def DFS(lst, start):
     stack = [start]
     visited = []
     order = ''

     while stack:
         crnt_node = stack.pop()
         if crnt_node not in visited:
             visited.append(crnt_node)
             order += str(crnt_node) + ' '
             for children in lst[crnt_node]:
                 if children not in visited:
                     stack.append (children)
     return order

result=DFS(lst,1)
for i in result:
    f2.write(f'{i}')
    print(i,end='')
