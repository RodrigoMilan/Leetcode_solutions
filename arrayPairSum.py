class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        valor = 0
        for i in range(0,len(nums)-1,2):
            valor += min(nums[i],nums[i+1])
        return valor
