class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if len(set(substr)) == len(substr):
                    l = max(l, len(substr))
                else:
                    break

        return l
        