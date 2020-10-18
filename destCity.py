class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        all_destinations = []
        all_origins  = []
        
        for [city1,city2] in paths:
            all_origins.append(city1)
            all_destinations.append(city2)
            
        return [d for d in all_destinations if d not in all_origins][0]
