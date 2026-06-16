class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each string
        # map<string, list>
        # append to list value to each corresponding key
        # return list(map.values())?
        anagrams = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in anagrams:
                anagrams.get(key).append(s)
            else:
                anagrams[key] = [s]

        return list(anagrams.values())