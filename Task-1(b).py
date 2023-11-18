f1=open('input-1(b).txt','r')
f2=open('output-1(b).txt','w')
N,M=map(int,f1.readline().split( ))
lst=[[]for i in range(N+1)]
for i in range(M):
    v,e,w=map(int,f1.readline().split())
    lst[v].append(f'{e,w}')

for j in range(N+1):

    value = ' '.join(lst[j])
    print(f'{j}:{value}')
    f2.write(f'{j}: {value}\n')


f2.close()
f1.close()

