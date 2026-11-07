class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        idk = [1] * len(nums)
        prefix = 1 
        for n in range(len(nums)):
            idk[n] = prefix
            prefix *= nums[n]
        postfix = 1 
        for k in range(len(nums) -1, -1, -1 ):
            idk[k] *= postfix
            postfix *= nums[k]
        return idk
