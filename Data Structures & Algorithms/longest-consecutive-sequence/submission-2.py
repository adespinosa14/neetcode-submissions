class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        sets = []
        max = 0

        for n in nums:
            if n - 1 not in nums:
                sets.append([n])

        for s in sets:
            index = 0
            while s[index] + 1 in num_set:
                s.append(s[index] + 1)
                index += 1
            if max < len(s):
                max = len(s)

        return max
        