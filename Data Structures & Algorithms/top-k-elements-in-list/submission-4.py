class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        base_dict = {}
        for num in nums:
            base_dict[num] = 1 + base_dict.get(num, 0)
        sorted_list = sorted(base_dict.items(), key=lambda x: -x[1])
        res_list = [key for key,value in sorted_list[:k]]
        return res_list
        