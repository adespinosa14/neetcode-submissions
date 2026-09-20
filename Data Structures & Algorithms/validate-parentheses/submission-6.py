class Solution:
    def isValid(self, s: str) -> bool:

        res = []

        for c in s:
            match c:
                case ']':
                    if res and res[-1] == '[':
                        res.pop()
                        continue
                case ')':
                    if res and res[-1] == '(':
                        res.pop()
                        continue
                case '}':
                    if res and res[-1] == '{':
                        res.pop()
                        continue
            res.append(c)

        return True if len(res) == 0 else False
