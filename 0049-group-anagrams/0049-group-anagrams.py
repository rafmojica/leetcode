class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            letterFreq = tuple(count)
            if letterFreq in freq:
                freq.get(letterFreq).append(s)
            else:
                freq[letterFreq] = [s]

        return list(freq.values())
