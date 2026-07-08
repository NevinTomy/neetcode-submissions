class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            pos = [0] * 26
            for wrd in s:
                pos[ord(wrd) - ord('a')] += 1
            res[tuple(pos)].append(s)
        return list(res.values())

