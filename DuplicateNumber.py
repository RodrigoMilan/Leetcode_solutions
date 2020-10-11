#287. Find the Duplicate Number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        self.nums = nums
        pre = []
        for i in nums:
            if i in pre:
                return i
            else:
                pre.append(i)