class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = re.sub(r'[^a-zA-Z0-9]+', '', s)
        s_new = s_new.lower()

        l, r = 0, len(s_new) - 1

        while l < r:
            if s_new[l] == s_new[r]:
                l += 1
                r -= 1
            else:
                return False
        return True