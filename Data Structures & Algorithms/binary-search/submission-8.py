class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            half = (l + r) // 2
            
            if nums[half] == target: return half
            
            match target > nums[half]:
                case True:
                    l = half + 1
                case _:
                    r = half - 1
        
        return -1