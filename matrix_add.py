x=[[1,2,3],[3,2,1],[1,2,2]]
y=[[1,2,3],[3,2,1],[1,2,2]]
r=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        r[i][j]=x[i][j]+y[i][j]

print(r)
