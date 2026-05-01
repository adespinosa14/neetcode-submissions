class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        sets = []
        max_ = 0

        for n in nums:
            if n - 1 not in nums:
                sets.append([n])
                length = 0
                while (n + length) in num_set:
                    length += 1
                    max_ = max(length, max_) 

        return max_
        