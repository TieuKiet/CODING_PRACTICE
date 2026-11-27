import java.util.*;

public class MajorityElementII {
    public List<Integer> majorityElement(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        List<Integer> res = new ArrayList<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        int limit = nums.length / 3;
        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            int key = entry.getKey();
            int value = entry.getValue();

            if (value > limit) {
                res.add(key);
            }
        }
        
        return res;
    }
}
