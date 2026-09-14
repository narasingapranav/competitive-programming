class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = tuple(num for row in board for num in row)
        goal = (1,2,3,4,5,0)
        neighbors = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4],4:[1,3,5],5:[2,4]}
        
        queue = deque([(start,0)])
        visited = set()
        
        while queue:
            state, moves = queue.popleft()
            if state == goal:
                return moves
            if state in visited:
                continue
            visited.add(state)
            zero = state.index(0)
            for n in neighbors[zero]:
                lst = list(state)
                lst[zero], lst[n] = lst[n], lst[zero]
                queue.append((tuple(lst), moves+1))
        return -1        