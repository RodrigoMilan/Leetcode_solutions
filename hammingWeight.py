#Number of 1 Bits 
###Two solutions

from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = Counter(bin(n))
        return counter['1']

''' 28 ms and 14 MB'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
'''24 ms and 14.3Mb'''
