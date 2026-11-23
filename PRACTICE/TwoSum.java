import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;
public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        // freq: {value: index}
        Map<Integer, Integer> freq = new HashMap<>();
        
        for (int i = 0; i<nums.length; i++ ) {
            int cur = target - nums[i];
            
            if (freq.containsKey(cur)) {
                return new int[] {freq.get(cur), i};
            }
            freq.put(nums[i], i);
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        var sol = new TwoSum();
        var res = sol.twoSum(new int[] {1,2,3,4,5,6,7}, 8);
        System.out.println(Arrays.toString(res));
    }
}

