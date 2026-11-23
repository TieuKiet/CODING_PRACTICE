import java.util.Arrays;

public class RemoveElement {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }

    public static void main(String[] args) {
        var sol = new RemoveElement();
        int[] arr = new int[] {1,2,3,4,5};
        var res = sol.removeElement(arr, 4);
        System.out.println(res + "\n" + Arrays.toString(arr));
    }
}
