class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] answer = {0,0};
        for(int i = 0; i < nums.length; i++)
        {
            int diff = target - nums[i];

            if(map.containsKey(diff))
            {
                answer[0] = map.get(diff);
                answer[1] = i;
                return answer;
            }
            else
            {
                map.put(nums[i], i);
            }
        }

        return answer;
    }
}
