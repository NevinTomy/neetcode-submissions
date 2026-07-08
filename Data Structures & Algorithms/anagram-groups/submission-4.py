class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        base_dict = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in base_dict:
                base_dict[s_sorted].append(s)
            else:
                base_dict[s_sorted] = [s]
        return [value for key,value in base_dict.items()]