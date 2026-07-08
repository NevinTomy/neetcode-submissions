class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = 1 + d.get(i, 0)
        return [k for k,v in sorted(d.items(), key=lambda x: -x[1])][0:k]