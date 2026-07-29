class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # input: nums1 = [2, 3, 4], nums2 = [4, 3, 2, 5]
        # output: [5, 5, 5]
        # 1. initialize result array filled with -1 length of nums1
        # 2. iterate through nums2, create hashmap where key = element, value = next greater element 
        # 3. create stack and append each element index in monotonic decreasing order.
        # 4. iterate through nums1, access each value and append to result, -1 otherwise if no pairing.

        stack = []
        res = []
        pair = {}
        
        for num in nums2:
            while stack and num > stack[-1]:
                k = stack.pop()
                pair[k] = num       # { element: next greater element }
            stack.append(num)       # append otherwise
                
        for num in nums1:
            res.append(pair.get(num, -1))

        return res
        