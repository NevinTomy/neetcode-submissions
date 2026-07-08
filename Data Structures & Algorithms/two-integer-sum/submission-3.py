class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        left = 0
        right = len(nums) - 1
        while left < right:
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append(left)
                    res.append(right)
                    return res
                right -= 1
            left += 1
            right = len(nums) - 1
        
        