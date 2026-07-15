class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)

        for i in range(len(nums)):
            
            mid = (l + r) // 2
            
            if nums[mid] == target: return mid

            l, r = (mid, r) if target > nums[mid] else (l, mid)
            
        return -1