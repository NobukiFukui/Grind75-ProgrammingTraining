# 2-02_RandomNote
Author: WaveAlchemist  
URL: https://leetcode.com/problems/ransom-note/description/
description:
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

# 1st
242. Valid Anagramで利用したdefaultdictを用いたアルゴリズムを作成（解答時間 約20分, 実行時間　62ms）
- magazineのそれぞれの文字数をチェックし，char_countに格納
- ransomNoteについてそれぞれの文字をチェックし，該当する文字がある場合はchar_countから-1
- char_count[char]が0になった場合は，magazineに該当する文字が含まれていない，あるいは文字の数がransomNoteのほうが多いと判定

``` Python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # make default dictionary for counting character number in magazine
        char_count = defaultdict(int)
        # count number of each character
        for char in magazine:
            char_count[char] += 1
        # check if characters in ransomNote are included in magazine
        for char in ransomNote:
            if char_count[char] == 0:
                return False
            char_count[char] -= 1
        return True
```

