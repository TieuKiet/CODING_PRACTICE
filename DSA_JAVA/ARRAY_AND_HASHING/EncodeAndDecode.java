import java.util.ArrayList;
import java.util.List;

public class EncodeAndDecode {
    public String encode(List<String> strs) {
        // #strs[i]
        StringBuilder encode_str = new StringBuilder();
        for (String str : strs) {
            int length = str.length();
            encode_str.append(length);
            encode_str.append('#');
            encode_str.append(str);
        }

        return encode_str.toString();
    }

    public List<String> decode(String str) {
    List<String> res = new ArrayList<>();
    int i = 0;

    while (i < str.length()) {
        int j = i;
        // Cho j chạy tới khi đụng dấu '#'
        while (str.charAt(j) != '#') {
            j++;
        }

        // Đoạn từ i đến j-1 chính là con số độ dài (dù là "5" hay "123" đều cân hết)
        int len = Integer.parseInt(str.substring(i, j));

        // Cắt lấy chuỗi nội dung nằm ngay sau dấu '#' (tức là từ j + 1)
        String word = str.substring(j + 1, j + 1 + len);
        res.add(word);

        // Nhảy con trỏ i qua hết chuỗi vừa cắt để đọc phần tử tiếp theo
        i = j + 1 + len;
    }

    return res;
}

    public static void main(String[] args) {
        var sol = new EncodeAndDecode();
        var encode = sol.encode(List.of("tkiet123","gemini"));
        var decode = sol.decode(encode);
        System.out.println(decode);
    }
}
