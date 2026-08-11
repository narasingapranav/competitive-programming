class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        for i in range(n):
            if color[i] != -1:
                continue

            color[i] = 0
            queue = [i]
            front = 0

            while front < len(queue):
                node = queue[front]
                front += 1

                for nei in graph[node]:
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        return False

        return True