# ===============================================================
# (program) 02_ValidParentheses
# WaveAlchemist
# Description: 
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
# URL: https://leetcode.com/problems/valid-parentheses/description/
# ===============================================================

# %%
class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(0, len(s)-1, 2):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                if (s[i] == '(' and s[i+1] != ')') or (s[i] == '[' and s[i+1] != ']') or (s[i] == '{' and s[i+1] != '}'):
                    return False
            else:
                return False
            
            return True
                    


s = "()"
Solution.isValid([],s)


# %%
