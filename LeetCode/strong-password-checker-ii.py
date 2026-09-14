class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        l=u=d=s=False
        sp=set("!@#$%^&*()-+")
        prev=None
        for i in password:
            if i==prev:
                return False
            prev=i
            if i.islower():
                l=True
            elif i.isupper():
                u=True
            elif i.isdigit():
                d=True
            elif i in sp:
                s=True
        return l and u and d and s
