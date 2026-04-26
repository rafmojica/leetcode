class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        result = []

        # get every integer and their count
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # sort by ascending most frequent index
        for elem, val in count.items():
            freq[val].append(elem)

        for i in range(len(nums), 0, -1):
            # pop k elements in array and append to result.
            while len(result) < k and freq[i]:
                result.append(freq[i].pop())

        return result
