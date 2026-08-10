class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        sc=[0]*10
        gc=[0]*10
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
            else:
                sc[int(secret[i])]+=1
                gc[int(guess[i])]+=1
        cows=0
        for i in range(10):
            cows+=min(sc[i],gc[i])
        return str(bulls)+'A'+str(cows)+'B'