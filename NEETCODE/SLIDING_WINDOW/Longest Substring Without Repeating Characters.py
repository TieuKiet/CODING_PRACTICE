class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Lưu ký tự -> index gần nhất của nó
        left = 0
        max_len = 0

        for right, c in enumerate(s):
            # Nếu gặp ký tự trùng và vị trí cũ nằm trong cửa sổ hiện tại [left, right]
            if c in char_map and char_map[c] >= left:
                left = char_map[c] + 1  # Nhảy con trỏ left sang ngay sau vị trí trùng cũ

            char_map[c] = right  # Cập nhật vị trí mới nhất của c
            max_len = max(max_len, right - left + 1)

        return max_len