class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLen = 0
        cs = set()
        left = 0

        for right in range(n):
            if s[right] not in cs:
                cs.add(s[right])
                maxLen = max(maxLen, right - left + 1)
            else:
                while s[right] in cs:
                    cs.remove(s[left])
                    left += 1
                cs.add(s[right])
        return maxLen 