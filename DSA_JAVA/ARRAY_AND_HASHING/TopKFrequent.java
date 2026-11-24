import java.util.*;

public class TopKFrequent {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        List<List<Integer>> buckets = new ArrayList<>();
        for (int i = 0; i <= nums.length; i++) {
            buckets.add(new ArrayList<>());
        }

        for (var entry : freq.entrySet()) {
            buckets.get(entry.getValue()).add(entry.getKey());
        }

        int[] res = new int[k];
        int idx = 0;
        for (int i = buckets.size() - 1; i > 0; i--) {
            for (int num : buckets.get(i)) {
                res[idx++] = num;
                if (idx == k) {
                    return res;
                }
            }
        }
        return res;
    }
}