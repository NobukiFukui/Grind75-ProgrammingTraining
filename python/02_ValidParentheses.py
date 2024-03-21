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

# %% 2nd
# class Solution:
#     def isValid(self, s: str) -> bool:

#         stack_list = []
#         n_str = len(s)

#         for i in range(n_str):
#             if s[i] == '(' or s[i] == '{' or s[i] == '[':
#                 stack_list.append(s[i])
#             elif s[i] == ')' and stack_list != []:
#                 if stack_list[-1] != '(':
#                     return False
#                 stack_list.pop()
#             elif s[i] == '}' and stack_list != []:
#                 if stack_list[-1] != '{':
#                     return False
#                 stack_list.pop()
#             elif s[i] == ']' and stack_list != []:
#                 if stack_list[-1] != '[':
#                     return False
#                 stack_list.pop()
#             else:
#                 return False
#         if stack_list != []:
#             return False
#         else:
#             return True

# s = "()}"
# Solution.isValid([],s)


# %% 3rd


# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack_list = []
#         pairs = {"(": ")", "[": "]", "{": "}"}
#         n_str = len(s)
#         for bracket in s:
#             if bracket in pairs:
#                 stack_list.append(bracket)
#             else:
#                 if stack_list == [] or bracket != pairs[stack_list.pop()]:
#                     return False
#         if stack_list == []:
#             return True
#         else:
#             return False


# s = "("
# Solution.isValid([],s)
# %% 4th
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         pairs = {"(": ")", "[": "]", "{": "}"}
#         for bracket in s:
#             if bracket in pairs:
#                 stack.append(bracket)
#             else:
#                 if stack == [] or bracket != pairs[stack.pop()]:
#                     return False
#         if stack == []:
#             return True
#         else:
#             return False


# s = "("
# Solution.isValid([],s)

# %%
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs =  { ')': '(', '}': '{', ']': '[' } 
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if stack == []:
                    return False
                else:
                    if stack.pop() != pairs[ch]:
                        return False
        return stack == []


s = "("
Solution.isValid([],s)
# %%
