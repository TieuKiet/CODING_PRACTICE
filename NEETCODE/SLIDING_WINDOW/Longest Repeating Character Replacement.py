class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq= 0
        max_len = 0
        left = 0
        freq = freq= dict.fromkeys(s, 0)

        for right in range(len(s)):
            c = s[right]
            freq[c] += 1
            max_freq= max(max_freq, freq[c])

            if (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

        return len(s) - left

# A BBBABBCB