from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for x,y in counter.items():
            if y > 1:
                for i in range(y-1):
                    nums.remove(x)
