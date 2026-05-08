class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i, front in enumerate(nums):
            if front > 0: break

            if i > 0 and front == nums[i - 1]: continue

            left, right = i + 1, len(nums) - 1

            while left < right:

                addition = front + nums[left] + nums[right]

                if addition < 0: 
                    left += 1
                elif addition > 0: 
                    right -= 1
                elif addition == 0: 
                    res.append([front, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1


        return res

        