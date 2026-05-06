class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l_set = set(nums)
        res = 0

        for n in nums:
            length = 0
            if (n - 1) not in l_set:
                while( (n + length) in l_set):
                    length += 1
            res = max(res, length)

        return res

        