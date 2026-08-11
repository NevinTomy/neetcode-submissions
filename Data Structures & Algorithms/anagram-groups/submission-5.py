from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        base_dict = defaultdict(list)
        for s in strs:
            s_sorted = ''.join(sorted(s))
            base_dict[s_sorted].append(s)
        return list(base_dict.values())