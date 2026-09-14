import random
class RandomizedSet:

    def __init__(self):
        self.l=[]

    def insert(self, val: int) -> bool:
        if val in self.l:
            return False
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.l:
            return False
        a=self.l.pop(self.l.index(val))
        return True

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()