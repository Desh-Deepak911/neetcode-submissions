class Solution:
    def isPalindrome(self, s: str) -> bool:

        n = len(s) - 1
        i = 0

        while (i < n):
            if (not s[i].isalnum()):
                i = i + 1
                continue
            if (not s[n].isalnum()):
                n = n - 1
                continue
            if s[n].lower() == s[i].lower():
                i = i + 1
                n = n - 1
            else:
                return False
        
        return True