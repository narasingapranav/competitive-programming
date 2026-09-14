class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            n = num
            flag = True
            while n > 0:
                rem = n % 10
                if rem == 0 or num % rem != 0:
                    flag = False
                    break
                n //= 10
            if flag:
                result.append(num)
        return result