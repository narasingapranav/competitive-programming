class Trie:

    def __init__(self):
        self.child={}
        self.eow=False

    def insert(self, word: str) -> None:
        node=self
        for i in word:
            if i not in node.child:
                node.child[i]=Trie()
            node=node.child[i]
        node.eow=True

    def search(self, word: str) -> bool:
        node=self
        for i in word:
            if i not in node.child:
                return False
            node=node.child[i]
        return node.eow

    def startsWith(self, prefix: str) -> bool:
        node=self
        for i in prefix:
            if i not in node.child:
                return False
            node=node.child[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)