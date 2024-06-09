
# %%
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        # make default dictionary for counting character number in magazine
        char_count = defaultdict(int)
        # count number of each alphabet
        for char in magazine:
            char_count[char] += 1
        # check if alphabets in ransomNote are included in magazine
        for char in ransomNote:
            if char_count[char] == 0:
                return False
            char_count[char] -= 1
        return True

# %%
ransomNote = "v"
magazine = "aaaaaabbbbbb"
solution = Solution()
print( solution.canConstruct(ransomNote, magazine))
# %%
