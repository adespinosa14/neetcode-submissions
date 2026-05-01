class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++)
        {
            int current_value = nums[i];
            if(map.containsValue(current_value))
            {
                return true;
            }else
            {
                map.put(i, current_value);
            }
        }

        return false;
    }
}