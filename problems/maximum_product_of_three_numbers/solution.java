import java.util.Arrays;
class Solution {
    public int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        
        int firstTwoAndLast = nums[0] * nums[1] * nums[nums.length-1];
        int lastThreeValue = nums[nums.length-1] * nums[nums.length-2] * nums[nums.length-3];
        
        if(lastThreeValue > firstTwoAndLast) {
            return lastThreeValue;
        } 
        
        return firstTwoAndLast;
    }
}