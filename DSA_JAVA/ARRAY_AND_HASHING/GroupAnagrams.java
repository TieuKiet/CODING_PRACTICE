
import java.util.*;

public class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> check = new HashMap<>();

        for (String s : strs) {
            int[] count = new int[26];

            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }
            String key = Arrays.toString(count);

            if (!check.containsKey(key)) {
                check.put(key, new ArrayList<>());
            }

            check.get(key).add(s);
        }
        return new ArrayList<>(check.values());
    }
}
