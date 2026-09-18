class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        htable = {}
        res = []

        for i in range(len(nums)):
            htable[nums[i]] = i
        
        for i in htable:
            if (i - 1) not in htable:
                y = 0
                temp = []
                while i + y in htable:
                    temp.append(i + y)
                    y += 1
                res = res if len(res) > len(temp) else temp
            else:
                continue
        
        return len(res)
        