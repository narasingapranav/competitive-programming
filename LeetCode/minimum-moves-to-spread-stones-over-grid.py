class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        need, has = [], {}
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    need.append((i, j))
                if grid[i][j] > 1:
                    has[(i, j)] = grid[i][j]
        
        def go():
            if len(need) == 0: return 0
            best = inf
            i1, j1 = need.pop()
            for (i2, j2) in has.keys():
                if has[(i2, j2)] == 1:
                    continue
                has[(i2, j2)] -= 1
                cost = abs(i2 - i1) + abs(j2 - j1)
                best = min(best, go() + cost)
                has[(i2, j2)] += 1
            need.append((i1, j1))
            return best

        return go()