class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create a map for ransomNote and magazine respectively
        count = [0] * 26
        for c in magazine:
            count[ord(c) - ord('a')] += 1

        for c in ransomNote:
            count[ord(c) - ord('a')] -= 1

        for val in count:
            if val < 0:
                return False
        
        return True
