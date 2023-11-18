f1=open('input-1(a).txt','r')
f2=open('output-1(a).txt','w')
N,M=map(int,f1.readline().split( ))
mat=[[0 for i in range(N+1)]for j in range(N+1)]
for i in range(M):
    v,e,w= map(int,f1.readline().split())
    mat[v][e]=w
for i in range(N+1):
    for j in range(N+1):
        f2.write(f'{mat[i][j]} ')
    f2.write('\n')
f2.close()
f1.close()