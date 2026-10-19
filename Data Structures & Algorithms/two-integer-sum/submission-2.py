class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dics = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in dics:
                return [dics[diff], i]
            dics[v] = i