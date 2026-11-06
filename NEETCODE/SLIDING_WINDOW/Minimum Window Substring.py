from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        count_t = Counter(t)
        window= {}
        have, need = 0, len(count_t)
        res, min_len = [-1, -1], float("inf")
        left= 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            # Tăng have khi ký tự c đạt đủ số lượng t yêu cầu
            if c in count_t and window[c] == count_t[c]:
                have += 1

            # Khi cửa sổ thỏa mãn, thu hẹp left tối đa có thể
            while have == need:
                # Cập nhật cửa sổ nhỏ nhất
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res = [left, right]

                    
                # Bắt đầu loại bỏ s[left] khỏi cửa sổ
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        return s[l : r + 1] if min_len != float("inf") else ""

s= Solution()
print(s.minWindow(s = "OUZODYXAZV", t = "XYZ"))