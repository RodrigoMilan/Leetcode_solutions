class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        lista = []
        for i in arr:
            if i not in lista:
                lista.append(i)
        
        counter = {}
        
        for i in lista:
            counter[i] = 0
        
        for i in arr:
            counter[i] += 1
        
        length = len(counter.values())
        if len(set(counter.values())) == length:  
            return True
        else:
            return False
