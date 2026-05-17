class Solution {
    public int[] twoSum(int[] nums, int target) {
        int f = 0, l = nums.length-1;

        while(f<l) {
            int sum = nums[f]+nums[l];
            if(sum == target){
                return new int[]{f+1, l+1};
            }
            if(sum>target) l--;
            else f++;
        }
        return null;
    }
}