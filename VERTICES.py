import
A = "ABCDEFGHIJKLMNOPQRSTUVXWYZabcdefghijklmnopqrstuvxwyz0123456789"

b = int(input())
c = ''
c += "grafo = Grafo(["
for i in range(b):
    c += "'%s'" % A[i]

c += "], "

bd = []
while True:
    a = input()
    if a == "s":
        break
    bd.append(a)

c+= "{ "

for i in range(len(bd)):
    c += "'a%d' : '%s'," % (21+i, bd[i])

c = c[:-1] + "}]"

print(c)
