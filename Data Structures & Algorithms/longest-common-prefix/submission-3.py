class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1: return strs[0]
        if len(strs) == 0: return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            word = strs[i]
            if word == "": return ""
            
            for j in range(len(word)):
                if len(prefix) <= j: break

                if(word in prefix and len(prefix) > len(word)):
                    prefix = prefix[0:len(word)]

                if word[j] != prefix[j]:
                    prefix = prefix[0:j]


        return prefix
        