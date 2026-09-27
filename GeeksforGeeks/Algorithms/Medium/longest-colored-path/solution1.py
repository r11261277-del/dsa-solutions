from collections import deque, defaultdict

class Solution:
    #-----------------------------------------------------------
    def longestPath(self, s: str, edges):
    #-----------------------------------------------------------
        n = len(s)
        adj = [[] for _ in range(n)]
        for u, v in edges:           # convert to 0-based indices
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)

        # ------------------------------------------------------
        # helper: process one colour, return (far[], diameter_nodes)
        # ------------------------------------------------------
        def process(col: str):
            far   = [0] * n          # distance (edges) to farthest node
            seen  = [False] * n
            diameter_nodes = 0

            for src in range(n):
                if seen[src] or s[src] != col:
                    continue

                # 1) collect this component and mark seen
                comp = []
                q = deque([src])
                seen[src] = True
                while q:
                    u = q.popleft()
                    comp.append(u)
                    for v in adj[u]:
                        if not seen[v] and s[v] == col:
                            seen[v] = True
                            q.append(v)

                # empty component? impossible, at least src present
                # 2) BFS from arbitrary node -> farthest A
                def bfs(start):
                    dist = {start: 0}
                    q = deque([start])
                    far_node = start
                    while q:
                        u = q.popleft()
                        for v in adj[u]:
                            if s[v] != col or v in dist:
                                continue
                            dist[v] = dist[u] + 1
                            q.append(v)
                            if dist[v] > dist[far_node]:
                                far_node = v
                    return far_node, dist

                A, _        = bfs(src)        # first endpoint
                B, distA    = bfs(A)          # second endpoint + dist from A
                _, distB    = bfs(B)          # dist from B

                diameter_nodes = max(diameter_nodes, distA[B] + 1)

                # fill far[·] for this component
                for node in comp:
                    far[node] = max(distA.get(node, 0), distB.get(node, 0))

            return far, diameter_nodes
        # ------------------------------------------------------

        farRed,  redDiam  = process('R')
        farBlue, blueDiam = process('B')

        # ------------------------------------------------------
        # mix colour: test every R-B edge
        # ------------------------------------------------------
        best_mix = 0
        for u, v in edges:
            u -= 1
            v -= 1
            if s[u] == 'R' and s[v] == 'B':
                best_mix = max(best_mix, farRed[u] + farBlue[v] + 2)
            elif s[u] == 'B' and s[v] == 'R':
                best_mix = max(best_mix, farRed[v] + farBlue[u] + 2)

        return max(redDiam, blueDiam, best_mix)