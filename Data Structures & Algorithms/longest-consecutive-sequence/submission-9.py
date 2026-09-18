class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        htable = {}
        top = []
        res = []
        temp = []

        for i in range(len(nums)):
            htable[nums[i]] = i
        
        for i in htable:
            if (i - 1) not in htable:
                y = 0
                while i + y in htable:
                    temp.append(i + y)
                    y = y + 1
                res = res if len(res) > len(temp) else temp
                temp = []
            else:
                continue
        
        
        return len(res)
        