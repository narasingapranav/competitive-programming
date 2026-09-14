from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0)) 
                elif grid[r][c] == 1:
                    fresh_count += 1
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        time_elapsed = 0
        while queue:
            x, y, time = queue.popleft()
            time_elapsed = max(time_elapsed, time)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh_count -= 1
                    queue.append((nx, ny, time + 1))

        return time_elapsed if fresh_count == 0 else -1
