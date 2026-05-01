class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap <Integer, Integer> map = new HashMap<>();
        int[] answer_arr = {0,0};

        for(int i = 0; i < nums.length; i++)
        {
            int current_value = nums[i];
            int diff = target - current_value;

            if(map.containsKey(diff))
            {
                answer_arr[0] = map.get(diff);
                answer_arr[1] = i;
            }
            else
            {
                map.put(nums[i], i);
            }
        }

        return answer_arr;
    }
}
