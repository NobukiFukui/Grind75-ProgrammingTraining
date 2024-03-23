# ===============================================================
# (program) 05_ValidPalindrome
# WaveAlchemist
# Description: 
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# ===============================================================

# %% 1st
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filter() 関数を文字列に適用
        s_filtered = filter(str.isalnum, s)
        s = "".join(s_filtered)
        s_lower = s.lower()
        len_s = len(s)
        for i in range(int(len_s/2)):
            if s_lower[i] != s_lower[-i-1]:
                return False
        return True

s = "iiiiiik:iiiiii"
Solution.isPalindrome([],s)

# %%
