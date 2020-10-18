class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        self.nums = List
        self.n = n
        
        x = nums[:n]
        y = nums[n:]
        
        outp = []
        for x, y in zip(x,y):
            outp.append(x)
            outp.append(y)
        
        return outp
