class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            l = 0
            r = len(nums) - 1
            prod = 1
            while l < i:
                prod *= nums[l]
                l += 1
            while r > i:
                prod *= nums[r]
                r -= 1
            res.append(prod)
        return res