class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for k in range(len(nums)):
                sumsx = nums[i] + nums[k]
                if i !=k:
                    if sumsx == target:
                        return [i, k]