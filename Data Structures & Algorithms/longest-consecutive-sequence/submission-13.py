class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        htable = {}
        longest = 0

        for i in range(len(nums)):
            htable[nums[i]] = i
        
        for i in htable:
            if (i - 1) not in htable:
                length = 0
                while i + length in htable:
                    length += 1
                
                longest = longest if longest > length else length
            else:
                continue
        
        return longest
        