class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = {}
        longest = 0
        
        for num in nums:
            numMap[num] = num
        
        for num in numMap:
            if (num - 1) not in numMap:
                length = 1
                while (num + length) in numMap:
                    length += 1
                longest = longest if longest > length else length
        
        return longest