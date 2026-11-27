import java.util.*;

public class ProductExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int prefix = 1;
        int n = nums.length;
        int[] res = new int[n];
        Arrays.fill(res, 1);

        for (int i = 0; i < n; i++) {
            res[i] *= prefix;
            prefix *= nums[i];
        }

        int suffix = 1;
        for (int i = n - 1; i > -1; i--) {
            res[i] *= suffix;
            suffix *= nums[i];
        }
        
        return res;
    }

    public static void main(String[] args) {
        var sol = new ProductExceptSelf();
        var res = sol.productExceptSelf(new int[] {1,2,4,6});
        System.out.println(Arrays.toString(res));
    }
}
