class Solution:
    def customSortString(self, order: str, s: str) -> str:

        c_map = {}
        res = []

        for c in s:
            c_map[c] = 1 + c_map.get(c, 0)

        for c in order:
            if c in c_map:
                for i in range(c_map[c]):
                    res.append(c)
                c_map.pop(c)

        for c in c_map:
            for i in range(c_map[c]):
                res.append(c)

        answer = "".join(res)

        return answer
        