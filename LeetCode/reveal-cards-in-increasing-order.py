class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        dq=deque()
        n=len(deck)
        for i in range(n):
            dq.append(i)
        res=[0]*n
        for i in range(n):
            x=dq.popleft()
            res[x]=deck[i]
            if dq :
                dq.append(dq.popleft())
        return res