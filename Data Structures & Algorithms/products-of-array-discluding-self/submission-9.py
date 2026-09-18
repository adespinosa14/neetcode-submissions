class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the res array, and make it as large as nums initializing each element to 1
        res = [1] * len(nums)

        # Initialize the prefix variable to 1
        prefix = 1

        # Iterate through res forward
        for i in range(len(res)):
            res[i] *= prefix
            prefix *= nums[i]

        # Initialize the postfix variable to 1
        postfix = 1
        
        # Iterate through res backwards
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        #Return res
        return res