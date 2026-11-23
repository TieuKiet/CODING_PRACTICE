import java.util.HashMap;
import java.util.Map;

public class HasDuplicate {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            if (freq.containsKey(num)) {
                return true;
            }
            freq.put(num, 1);
        }
        return false;
    }

    public static void main(String[] args) {
        var sol = new HasDuplicate();
        var res = sol.hasDuplicate(new int[] {1,2,3,4,4});
        System.out.println(res);
    }
}
