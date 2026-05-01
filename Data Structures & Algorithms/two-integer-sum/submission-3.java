class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap <Integer, Integer> map = new HashMap<>();
        int[] answer = {0,0};

        for(int i = 0; i < nums.length; i++)
        {

            int current_value = nums[i];
            int difference = target - current_value;

            if(map.containsKey(difference))
            {
                answer[0] = map.get(difference);
                answer[1] = i;
            }else
            {
                map.put(current_value, i);
            }

        }

        return answer;
    }   
}
