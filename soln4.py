#initializing the matrix
matrix= [[1,0,0,1,1],[1,0,0,0,1],[1,0,0,1,1],[1,1,1,1,1]]

x= [255,255]
y= [255,0]
m = [0,255]
n = [0,0]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            if x[0] > i:
                x[0] = i
            if x[1] > j:
                x[1] = j
            if x[0] > i:
                x[0] = i
            if x[1] < j:
                x[1] = j
            if m[0] < i:
                m[0] = i
            if m[1] > j:
                m[1] = j
            if n[0] < i:
                n[0] = i
            if n[1] < j:
                n[1] = j

if x[1] != n[1]:
    x[1] = min(x[1],m[1])
    m[1] = min(x[1],m[1])
if x[0] != y[0]:
    x[0] = min(x[0],y[0])
    y[0] = min(x[0],y[0])
if y[1] != n[1]:
    y[1] = max(y[1],n[1])
    n[1] = max(y[1],n[1])
if m[0] != n[0]:
    m[0] = max(m[0],n[0])
    n[0] = max(m[0],n[0])
print(x,y,m,n)
