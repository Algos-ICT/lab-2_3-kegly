import math
import time

inp = open("input.txt")

c_nodes, c_ribs = map(int, inp.readline().split())
edges = []

for _ in range(c_ribs):
    node, link, weight = map(int, inp.readline().split())
    edges.append((node - 1, link - 1, weight))

src, dst = map(int, inp.readline().split())
src -= 1
dst -= 1

inp.close()

ways = [None] * c_nodes
ways[src] = 0

start = time.time()
for i in range(c_nodes - 1):
    for source, destination, weight in edges:
        if ways[source] is not None:
            ways[destination] = min((math.inf if (ways[destination] is None) else ways[destination]),
                                    ways[source] + weight)
end = time.time()

out = open("output.txt", "w")
print(f"Answer: {ways[dst]}, Time: {end - start}")
if ways[dst] is None:
    out.write("-1")
else:
    out.write(str(ways[dst]))
out.close()
