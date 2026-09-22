from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = Counter(nums)
        return [k for k,v in sorted(hmap.items(), key=lambda x:-x[1])[:k]]
