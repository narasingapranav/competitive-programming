class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset=set(wordList)
        if endWord not in wordset:
            return []
        parents=defaultdict(list)
        visited=set()
        found=False
        level={beginWord}
        while level and not found:
            nextlevel=set()
            for i in level:
                visited.add(i)
            for w in level :
                for i in range(len(w)):
                    for ch in 'qwertyuiopasdfghjklzxcvbnm':
                        if ch== w[i]:
                            continue
                        newword=w[:i]+ch+w[i+1 :]
                        if newword in wordset and newword not in visited:
                            if newword == endWord:
                                found =True
                            nextlevel.add(newword)
                            parents[newword].append(w)
            level=nextlevel
        path=[endWord]
        res=[]
        def back(endWord):
            if endWord==beginWord:
                res.append(path[::-1])
                return
            for parent in parents[endWord]:
                path.append(parent)
                back(parent)
                path.pop()
        if found:
            back(endWord)
        return res