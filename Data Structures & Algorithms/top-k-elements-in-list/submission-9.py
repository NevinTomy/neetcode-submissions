class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)
        return [k for k,v in sorted(hmap.items(), key=lambda x:-x[1])[:k]]
