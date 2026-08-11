from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        base_dict = Counter(nums)
        sorted_dict = sorted(base_dict.items(), key=lambda x: -x[1])
        res = [k for k,v in sorted_dict[:k]]
        return res