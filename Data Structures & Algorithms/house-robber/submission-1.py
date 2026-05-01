class Solution:
    def rob(self, nums: List[int]) -> int:
        
        index = len(nums)
        memo = {}

        return self.dp(nums, index, memo)
    
    def dp(self, nums: List[int], n: int, memo) ->int:

        if n <= 0:
            return 0

        if n in memo:
            return memo[n]

        # Find max money
        money = max(
                    self.dp(nums, n - 1, memo),
                    nums[n - 1] + self.dp(nums, n - 2, memo)
                    )
        memo[n] = money

        return money


        