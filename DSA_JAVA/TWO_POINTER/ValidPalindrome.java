public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() -1;
        while (l < r) {
            if (!(Character.isLetterOrDigit(s.charAt(l)))) {l++;}
            else if (!(Character.isLetterOrDigit(s.charAt(r)))) {r--;}
            
            else {
                if ((Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r)))) {return false;}
                l++;
                r--;
            }
            
        }
        return true;
        
    }

    public static void main(String[] args) {
        var sol = new ValidPalindrome();
        String s = "Was it a car or a cat I saw?";
        var res = sol.isPalindrome(s);
        System.out.println(res);
    }
}