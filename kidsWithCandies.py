class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        outp = []
        for i in candies:
            if int(i) + extraCandies >= max_candies:
                outp.append(True)
            else:
                outp.append(False)
        
        return outp
