class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            half = (l + r) // 2
            if nums[half] == target: return half

            if target > nums[half]:
                l = half + 1
                continue

            if target < nums[half]:
                r = half - 1
                continue
        
        return -1