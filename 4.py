import sys

f = open('input.txt')

n, m = map(int, f.readline().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)


def explore(v, visited, stack):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            explore(i, visited, stack)
    stack.insert(0, v)


def dfs(G):
    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            explore(i, visited, stack)
    return stack


print(*map(lambda x: x + 1, dfs(graph)), sep=' ')