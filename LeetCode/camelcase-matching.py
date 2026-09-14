class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(query, pattern):
            j = 0  # pointer for pattern
            for c in query:
                if j < len(pattern) and c == pattern[j]:
                    j += 1
                elif c.isupper():
                    return False
            return j == len(pattern)

        return [match(q, pattern) for q in queries]        