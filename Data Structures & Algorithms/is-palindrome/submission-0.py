import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        l = 0
        r = len(s_cleaned) - 1
        while l < r:
            if s_cleaned[l] != s_cleaned[r]:
                return False
            l += 1
            r -= 1
        return True
        