class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_map = {}

        for index, num in enumerate(nums, 0):
            
            difference = target - num
            if difference in n_map:
                res_one = n_map.get(difference)
                res_two = index

                return [res_one, res_two]

            n_map[num] = index