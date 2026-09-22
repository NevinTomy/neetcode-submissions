class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {')':'(', ']':'[', '}':'{'}
        stack = []

        for chr in s:
            if chr in hmap.values():
                stack.append(chr)
            elif chr in hmap:
                if not stack or hmap[chr] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack