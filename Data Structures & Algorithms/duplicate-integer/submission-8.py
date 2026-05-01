class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for i in range(len(nums)):

            if nums[i] in map and map != {}:
                return True

            map[nums[i]] =  0

        return False