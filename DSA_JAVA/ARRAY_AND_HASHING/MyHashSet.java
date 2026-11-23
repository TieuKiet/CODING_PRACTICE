import java.util.*;

class MyHashSet {
    private List<Integer> arr;
    public MyHashSet() {
        this.arr = new ArrayList<>();
    }
    
    public void add(int key) {
        if (!contains(key)) {
            this.arr.add(key);
        }
    }
    
    public void remove(int key) {
        this.arr.remove(Integer.valueOf(key));
    }
    
    public boolean contains(int key) {
        return this.arr.contains(key);
    }

    public static void main(String[] args) {
        MyHashSet myHashSet = new MyHashSet();
        myHashSet.add(1);                            // set = [1]
        myHashSet.add(2);                            // set = [1, 2]
        System.out.println(myHashSet.contains(1));   // in ra: true
        System.out.println(myHashSet.contains(3));   // in ra: false
        myHashSet.add(2);                            // set = [1, 2]
        System.out.println(myHashSet.contains(2));   // in ra: true
        myHashSet.remove(2);                         // set = [1]
        System.out.println(myHashSet.contains(2));   // in ra: false
        
        // Nếu muốn in cả danh sách phần tử hiện có trong set để kiểm tra:
        System.out.println(myHashSet.arr);           // in ra: [1]
    }
}
