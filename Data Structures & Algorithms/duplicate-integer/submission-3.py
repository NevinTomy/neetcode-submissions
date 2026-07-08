class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        base_dict = {}
        for num in nums:
            if num in base_dict:
                return True
            else:
                base_dict[num] = 1
        return False