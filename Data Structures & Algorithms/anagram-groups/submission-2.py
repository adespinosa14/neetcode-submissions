class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            s_map = {}
            
            for char in s:
                s_map[char] = 1 + s_map.get(char, 0)

            key = tuple(sorted(s_map.items()))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())
        