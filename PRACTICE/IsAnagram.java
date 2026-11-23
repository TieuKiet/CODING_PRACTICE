import java.util.HashMap;
import java.util.Map;

public class IsAnagram {
public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            if (freq.getOrDefault(c, 0) == 0) {
                return false;
            }
            freq.put(c, freq.get(c) - 1);
        }

        return true;
    }

    public static void main(String[] args) {
        var sol = new IsAnagram();
        var res = sol.isAnagram("abcd", "dbca");
        System.out.println(res);
    }
}
