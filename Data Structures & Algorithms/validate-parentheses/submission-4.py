class Solution:
    def isValid(self, s: str) -> bool:
        hMap = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        for c in s:
            if c in hMap.values():
                stack.append(c)
            if c in hMap:
                if not stack or hMap[c] != stack[-1]:
                    return False
                stack.pop()
        return not stack 