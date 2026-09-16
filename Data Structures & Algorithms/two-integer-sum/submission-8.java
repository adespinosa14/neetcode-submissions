class Solution 
{
    public int[] twoSum(int[] nums, int target) 
    {
        Map<Integer, Integer> cache = new HashMap<Integer, Integer>();
        int[] res = new int[2];
        for(int i = 0; i < nums.length; i++)
        {
            int golden_num = target - nums[i];
            if (cache.containsKey(golden_num) )
            {
                res[0] = cache.get(golden_num);
                res[1] = i;

                return res;
            }
            cache.put(nums[i], i);
        }
        return res;
    }
}
