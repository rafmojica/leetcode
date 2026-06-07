class Solution:
    def countElements(self, arr: List[int]) -> int:
        # use hashmap to check if element exists in O(1) time
        # if x + 1 already exists in the set, add 1 to output
        # two for loops? O(2n) time
        
        dic = {}
        output = 0
        for i, v in enumerate(arr):
            dic[v] = i
            
        for num in arr:
            if num + 1 in dic:
                output += 1
        
        return output
        