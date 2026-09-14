class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n = bin(n)[2:]
        rev = ''
        for i in n:
            if i == '1':
                rev += '0'
            else:
                rev += '1'
        return int(rev, 2)