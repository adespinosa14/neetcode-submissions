class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26

            for c in s:
                char_diff = ord(c) - ord('a')
                count[char_diff] += 1
            
            res[tuple(count)].append(s)

        return list(res.values())