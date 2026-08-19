class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(set)
        for r, c in reservedSeats:
            reserved[r].add(c)
        possibilities = [
            [2, 3, 4, 5],
            [4, 5, 6, 7],
            [6, 7, 8, 9]
        ]
        c = 2 * n
        for r, seats in reserved.items():
            used = [False] * 3
            for k in range(3):
                possible = True
                for seat in possibilities[k]:
                    if seat in seats:
                        possible = False
                        break
                if possible:
                    used[k] = True
            if used[0] and used[2]:
                continue
            elif used[0] or used[1] or used[2]:
                c -= 1
            else:
                c -= 2
        return c