class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_new = re.sub(r'[^a-zA-Z0-9]+', '', s)
        s_new = s_new.lower()
        
        lpointer, rpointer = 0, len(s_new) - 1
        while lpointer < rpointer:
            if s_new[lpointer] == s_new[rpointer]:
                lpointer, rpointer = lpointer + 1, rpointer - 1
            else:
                return False
        return True
        