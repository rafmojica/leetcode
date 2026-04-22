class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = re.sub(r'[^a-zA-Z0-9]+', '', s)
        s_new = s_new.lower()

        if not s_new:
            return True

        # two pointers
        l = 0
        r = len(s_new) - 1

        while s_new[l] == s_new[r] and l < r:
            l += 1
            r -= 1

        return l >= r
        