class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''
        for i in digits:
            a += str(i)

        n = str(int(a) + 1)
        g = []
        for i in n:
            g.append(int(i))
        return g