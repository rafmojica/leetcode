class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # paths[i][0] = from
        # paths[i][1] = destination
        itinerary = {}
        
        for path in paths:
            itinerary[path[0]] = path[1]
        
        # check if path[1] is in itinerary
        for path in paths:
            if path[1] not in itinerary:
                return path[1]