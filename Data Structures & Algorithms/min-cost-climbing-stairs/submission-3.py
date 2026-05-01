class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        return self.dp(cost, n, memo)

    def dp(self, cost: List[int], n: int, memo) ->int:
        
        # Last Step
        if n <= 1:
            return 0

        if n in memo:
            return memo[n]
        
        # Calculate Steps
        steps = min(cost[n - 1] + self.dp(cost, n - 1, memo), 
                    cost[n - 2] + self.dp(cost, n - 2, memo))

        memo[n] = steps

        # Return        
        return steps
        