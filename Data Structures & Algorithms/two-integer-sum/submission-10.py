class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        base_dict = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in base_dict:
                return [base_dict[diff], i]
            else:
                base_dict[nums[i]] = i