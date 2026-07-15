class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f, l = 0, len(nums)

        for i in range(len(nums)):
            half = (f + l) // 2

            print(f"{f} {l}")

            if nums[half] == target: return half

            if target < nums[half]:
                l = half
            else:
                f = half
        
        return -1
        