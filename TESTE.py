

V = input().split(",")
a = input().split(",")

M = []
for k in range(len(V)):
    M.append(list())
    for l in range(len(V)):
        if k > l:
            M[k].append('-')
        else:
            M[k].append(0)

for i in a:
    M[V.index(i[-3])][V.index(i[-1])] += 1

print(M)
