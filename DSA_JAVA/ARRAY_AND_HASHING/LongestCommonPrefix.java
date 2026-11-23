public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder res = new StringBuilder();
        String minStr = strs[0];
        int n = minStr.length();

        for (String str : strs) {
            if (str.length() < n) {
                n = str.length();
                minStr = str;
            }
        }

        for (int i = 0; i < n; i++) {
            for (String str : strs) {
                if (minStr.charAt(i) != str.charAt(i)) {
                    return res.toString();
                }
            }
            res.append(minStr.charAt(i));
        }

        return res.toString();
    }

    public static void main(String[] args) {
        var sol = new LongestCommonPrefix();
        var res = sol.longestCommonPrefix(new String[] {"abcd", "ab", "abc"});
        System.out.println(res);
    }
}
