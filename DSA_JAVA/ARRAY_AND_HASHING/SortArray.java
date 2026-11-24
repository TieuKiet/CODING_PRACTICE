import java.util.*;
class SortArray {
    private void mergeSort(int[] nums, int[] temp, int left, int right) {
        if (left >= right) {
            return; // Mảng con còn 0 hoặc 1 phần tử thì dừng
        }

        int mid = (left + right) >>> 1;
        mergeSort(nums, temp, left, mid);        // Sắp xếp nửa trái
        mergeSort(nums, temp, mid + 1, right);   // Sắp xếp nửa phải
        merge(nums, temp, left, mid, right);     // Gộp 2 nửa đã sắp xếp
    }

    private void merge(int[] nums, int[] temp, int left, int mid, int right) {
        // Chép đoạn cần gộp từ mảng gốc sang mảng tạm
        for (int idx = left; idx <= right; idx++) {
            temp[idx] = nums[idx];
        }

        int i = left;      // Con trỏ duyệt nửa trái [left .. mid]
        int j = mid + 1;   // Con trỏ duyệt nửa phải [mid + 1 .. right]
        int k = left;      // Con trỏ ghi đè kết quả vào mảng gốc nums

        // So sánh từng cặp phần tử ở 2 nửa và đưa số nhỏ hơn vào nums
        while (i <= mid && j <= right) {
            if (temp[i] <= temp[j]) {
                nums[k++] = temp[i++];
            } else {
                nums[k++] = temp[j++];
            }
        }

        // Nếu nửa trái còn dư phần tử thì chép nốt vào nums
        while (i <= mid) {
            nums[k++] = temp[i++];
        }
    }
    
    public int[] sortArray(int[] nums) {
        int[] temp = new int[nums.length];
        mergeSort(nums, temp, 0, nums.length - 1);
        return nums;
    }

    public static void main(String[] args) {
        var sort = new SortArray();
        int[] arr = new int[] {7,3,1,8,9,6,4,2,5,8,0,5,3,5,7,2};
        int[] res = sort.sortArray(arr);
        System.out.println(Arrays.toString(res));

    }
}