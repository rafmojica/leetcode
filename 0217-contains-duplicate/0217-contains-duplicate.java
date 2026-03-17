class Solution {
    public boolean containsDuplicate(int[] nums) {
        // O(n) solution
        Map<Integer, Integer> numsMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (!numsMap.containsKey(nums[i]))
                numsMap.put(nums[i], 1);
            else
                return true;
        }
        return false;
    }
}