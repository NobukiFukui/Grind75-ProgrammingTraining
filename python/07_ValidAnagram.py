class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sSet = set(s)
        for ch in sSet:
            if s.count(ch) != t.count(ch):
                return False
        return True