class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        base_dict = {}
        for i in nums:
            if i in base_dict:
                base_dict[i] += 1
            else:
                base_dict[i] = 1
        sorted_list = sorted(base_dict.items(), key=lambda x: -x[1])
        res_list = [k for k,v in sorted_list[:k]]
        return res_list
        