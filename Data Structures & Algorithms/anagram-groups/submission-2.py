class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            pos = [0] * 26
            for wrd in s:
                pos[ord(wrd) - ord('a')] += 1
            if tuple(pos) in res:
                res[tuple(pos)].append(s)
            else:
                res[tuple(pos)] = [s]
        return list(res.values())

