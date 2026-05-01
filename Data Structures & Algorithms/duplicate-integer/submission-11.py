class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_map = {}

        for index, n in enumerate(nums, 0):
            if n in n_map: return True
            n_map[n] = index

        return False