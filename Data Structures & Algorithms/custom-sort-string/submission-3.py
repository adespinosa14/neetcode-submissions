class Solution:
    def customSortString(self, order: str, s: str) -> str:
        word = ""

        for c in order:
            for cs in s:
                if cs == c:
                    word += cs

        for c in s:
            if c not in order:
                word += c

        return word