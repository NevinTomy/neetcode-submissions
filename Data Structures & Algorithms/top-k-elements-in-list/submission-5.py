class Solution:
    def quick_sort(self, nums):
        n = len(nums)
        if n <= 1: return nums

        pivot = nums[n // 2]
        left = [x for x in nums if x[1] < pivot[1]]
        middle = [x for x in nums if x[1] == pivot[1]]
        right = [x for x in nums if x[1] > pivot[1]]
        return self.quick_sort(right) + middle + self.quick_sort(left)
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = 1 + res.get(num, 0)
        sorted_l = self.quick_sort(list(res.items()))
        return [key for key,value in sorted_l[:k]]