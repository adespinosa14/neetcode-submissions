class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        answer:int = 0
        p1 = 0
        p2 = 0

        while p1 < len(s):
            temp_str = ""

            for c in s[p1:]:
                if c in temp_str:
                    answer = max(len(temp_str), answer)
                    break
                
                temp_str += c
            answer = max(len(temp_str), answer)
            p1 += 1
        
        return answer

        