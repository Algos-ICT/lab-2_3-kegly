import math

inp = open("input.txt")

c_ribs = int(inp.readline())

edges = []
ways = {}

for _ in range(c_ribs):
    node, trash, link = inp.readline().split()
    edges.append((node, link, 1))
    if(node not in ways.keys()):
        ways[node] = None
    if(link not in ways.keys()):
        ways[link] = None

src = inp.readline().removesuffix("\n")
dst = inp.readline().removesuffix("\n")

inp.close()

ways[src] = 0

for i in range(len(ways.keys())):
    for source, destination, weigth in edges:
        if ways[source] is not None:
            ways[destination] = min((math.inf if (ways[destination] is None) else ways[destination]), ways[source] + weigth)

out = open("output.txt", "w")

if (dst not in ways.keys()) or (ways[dst] is None):
    out.write("-1")
else:
    out.write(str(ways[dst]))
out.close()

