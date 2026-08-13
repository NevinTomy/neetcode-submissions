class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {')':'(', '}':'{', ']':'['}
        op = []

        for chr in s:
            if chr in hmap.values():
                op.append(chr)
            elif chr in hmap:
                if not op or op[-1] != hmap[chr]:
                    return False
                op.pop()
        return not op