import collections
def cloneGraph2(self, node):  # BFS
    if not node:
        return node
    m = {node: Node(node.val)}
    deque = collections.deque([node])
    while deque:
        n = deque.popleft()
        for neigh in n.neighbors:
            if neigh not in m:
                deque.append(neigh)
                m[neigh] = Node(neigh.val)
            m[n].neighbors.append(m[neigh])
    return m[node]


def cloneGraph(self, node):  # DFS recursively
    if not node:
        return node
    m = {node: Node(node.val)}
    self.dfs(node, m)
    return m[node]


def dfs(self, node, m):
    for neigh in node.neighbors:
        if neigh not in m:
            m[neigh] = Node(neigh.val)
            self.dfs(neigh, m)
        m[node].neighbors.append(m[neigh])