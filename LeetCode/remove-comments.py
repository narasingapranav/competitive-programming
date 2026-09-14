class Solution:
    def removeComments(self, s: List[str]) -> List[str]:
        return [*filter(None,re.sub('//.*|/\*(.|\n)*?\*/','','\n'.join(s)).split('\n'))]