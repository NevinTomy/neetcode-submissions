class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {']':'[', '}':'{', ')':'('}

        for char in s:
            if char in hashMap.values():
                stack.append(char)
            elif char in hashMap:
                if not stack or stack[-1] != hashMap[char]:
                    return False
                stack.pop()
        return not stack