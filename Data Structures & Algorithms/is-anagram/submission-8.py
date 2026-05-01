class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        f_map = {}
        s_map = {}

        for index in range(len(s)):
            f_map[s[index]] = 1 + f_map.get(s[index], 0)
            s_map[t[index]] = 1 + s_map.get(t[index], 0)

        print(f_map)
        print(s_map)

        return f_map == s_map
        