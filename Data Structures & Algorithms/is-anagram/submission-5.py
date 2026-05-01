class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}

        for i in s:
            if i in map_s:
                map_s[i] += 1
            else:
                map_s[i] = 1

        for i in t:
            if i in map_t:
                map_t[i] += 1
            else:
                map_t[i] = 1
        
        return map_s == map_t