import java.util.Arrays;

class SortColor {

    private void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }

    public void sortColors(int[] nums) {
        int left = 0;
        int right = nums.length -1;
        int i = 0;
        while (i <= right) {
            if (nums[i] == 0) {
                swap(nums, i++, left++);
            }
            
            else if (nums[i] == 2) {
                swap(nums, i, right--);
            }

            else {
                i++;
            }
        }
    }

    public static void main(String[] args) {
        var sol = new SortColor();
        int[] arr = new int[] {1,1,1,0,0,0,2,2,2,1,2,2,1,2,0,0};
        sol.sortColors(arr);
        System.out.println(Arrays.toString(arr));
    }
}