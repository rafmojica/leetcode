class Solution:
    def isValid(self, s: str) -> bool:
        # at least one (), [], {} pair is guaranteed to be next to each other.
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace ('()', '')
            s = s.replace ('[]', '')
            s = s.replace ('{}', '')
        return s == ''