import java.util.*;

class MajorityElement {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        int max_freq = (int )nums.length / 2;
        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            int k = entry.getKey();
            int v = entry.getValue();

            if (v > max_freq) {
                return k;
            }
        }

        return 0;

    }

    public static void main(String[] args) {
        var sol = new MajorityElement();
        var res = sol.majorityElement(new int[] {5,5,1,1,1,5,5});
        System.out.println(res);
    }
}