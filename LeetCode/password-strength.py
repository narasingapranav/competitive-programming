class Solution:
    def passwordStrength(self, password: str) -> int:
        strength = 0
        seen = set()

        for ch in password:
            if ch not in seen:
                seen.add(ch)

                if 'a' <= ch <= 'z':
                    strength += 1

                elif 'A' <= ch <= 'Z':
                    strength += 2

                elif '0' <= ch <= '9':
                    strength += 3

                elif ch in "!@#$":
                    strength += 5

        return strength