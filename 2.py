import time

inp = open("input.txt")

c_nodes, c_ribs = map(int, inp.readline().split())

links = [[] for _ in range(c_nodes)]

for _ in range(c_ribs):
    node, link = map(int, inp.readline().split())
    links[node-1].append(link-1)
    links[link-1].append(node-1)

inp.close()

used = [False] * c_nodes
c_areas = 0

start = time.time()
for i in range(c_nodes):
    if not used[i]:
        c_areas += 1
        que = [i]
        used[i] = True
        while len(que) > 0:
            node = que.pop()
            for j in links[node]:
                if not used[j]:
                    que.append(j)
                    used[j] = True
end = time.time()

print(c_areas)
print(f"Time: {end-start}")

out = open("output.txt", "w")
out.write(str(c_areas))
out.close()

        
