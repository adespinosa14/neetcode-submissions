class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            current_num = nums[i]
            difference = target - current_num

            if difference in map:
                return [map[difference], i]

            map[current_num] = i