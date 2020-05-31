import copy
m = [[11, 12, 13, 14, 15],
     [21, 22, 23, 24, 25],
     [31, 32, 33, 34, 35],
     [41, 42, 43, 44, 45],
     [51, 52, 53, 54, 55]]
b = []
k = [0, 1, 0, 1, 0]
for i in range(len(m)):
    b.append(copy.deepcopy(m))

for i in range(0,len(m)):
    for j in range(0,len(m)):
        b[i][j][i] = k[j]
a = [[1,1,1],[2,2,2]]
def tr(a):
    c = []
    for i in range(len(a[0])):
        c.append([])
        for j in range(len(a)):
            c[i].append(0)
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[j][i]=a[i][j]
    return(c)
print(tr(a))