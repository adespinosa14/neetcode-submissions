class Solution {
    public int[] twoSum(int[] nums, int target) {

// Create answer array
// Create HashMap
// Iterate through the entire nums array
// Create one variables | difference
// If the difference is within the 

        int[] answer_array = {0,0};
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++)
        {
            int num = nums[i];
            int diff = target - num;

            if(map.containsKey(diff))
            {
                answer_array[0] = map.get(diff);
                answer_array[1] = i;
                break;
            }

            map.put(num, i);
        }

        return answer_array;
    }
}
