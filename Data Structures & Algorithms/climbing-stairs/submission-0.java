class Solution 
{
    Map<Integer, Integer> memo = new HashMap<>();
    public int climbStairs(int n) 
    {
        if(n <= 1) return 1;
        
        if (memo.containsKey(n))
            return memo.get(n);

        int step_one = climbStairs(n - 1);
        int step_two = climbStairs(n - 2);

        memo.put(n, step_one + step_two);

        return step_one + step_two;
    }
}
