class Solution:
    def countSegments(self, s: str) -> int:
        s=s.strip()
        if len(s)==0:
            return 0
        return len(s.split())