class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> check_duplicates = new HashMap<>();
        
        for(int i = 0; i < nums.length; i++)
        {
            
            if(check_duplicates.containsValue(nums[i]))
            {
                return true;
            }else
            {
                check_duplicates.put(i,nums[i]);
            }
        }

        return false;
    }
}