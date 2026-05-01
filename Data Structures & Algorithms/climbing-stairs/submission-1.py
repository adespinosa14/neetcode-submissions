class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        if n in self.memo:
            return self.memo.get(n)

        step_one = self.climbStairs(n - 1)
        step_two = self.climbStairs(n - 2)
        
        self.memo[n] = step_one + step_two

        return step_one + step_two
        
        