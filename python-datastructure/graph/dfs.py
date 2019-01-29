
from collections import namedtuple

Edge = namedtuple('Edge', ('vertex'))

def dfs(adj, visited, here):
    print(here)
    visited[here] = True
    
    for there in adj[here]:
        if not visited[there]:
            dfs(adj, visited, there)


def dfs_all(adj, visited, size):
    for here in range(size):
        if not visited[here]:
            dfs(adj, visited, here)


if __name__ == "__main__":
    adj = []
    size = 6

    for _ in range(0, size):
        adj.append([])

    adj[0].append(1)    
    adj[1].append(2)
    adj[1].append(3)
    adj[3].append(1)
    adj[3].append(4)
    adj[4].append(2)
    adj[5].append(3)

    visited = [False] * size
    dfs_all(adj, visited, size)
