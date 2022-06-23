inp = open("input.txt")

c_nodes, c_ribs = map(int, inp.readline().split())

links = [[] for _ in range(c_nodes)]

for _ in range(c_ribs):
    node, link = map(int, inp.readline().split())
    links[node - 1].append(link - 1)
    links[link - 1].append(node - 1)

src, trg = map(int, inp.readline().split())

src -= 1
trg -= 1

inp.close()

used = [False] * c_nodes
que = [src]

exist = False
used[src] = True
while len(que) > 0:
    node = que.pop()
    if node == trg:
        exist = True
        break
    for j in links[node]:
        if not used[j]:
            que.append(j)
            used[j] = True

out = open("output.txt", "w")
if exist:
    print("1")
    out.write("1")
else:
    print("0")
    out.write("0")
out.close()
