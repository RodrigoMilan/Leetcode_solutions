class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        inv = num[::-1]
        if num == inv:            
            return True
        else:
            return False
