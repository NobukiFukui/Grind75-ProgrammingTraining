# 02_ValidParentheses
Author: WaveAlchemist  
URL: https://leetcode.com/problems/valid-parentheses/description/


# 1st
方針：
配列sの左から順番に(か{か[があるかどうかをチェック
⇒いきなり)などの場合はFalseを返す
そうでない場合は右隣(i+1番目)の文字が)か]か}であれば，iのカウンタを増やす
⇒繰り返してFalseを返さない場合はTrueを返す

結果：
testcaseは実行できたが，submitの時点でwrong answerとなった．
s="{()}"のようにカッコ内にカッコがあるケースに対応ができない（Falseになってしまう）


```python
class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(0, len(s)-1, 2):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                if (s[i] == '(' and s[i+1] != ')') or (s[i] == '[' and s[i+1] != ']') or (s[i] == '{' and s[i+1] != '}'):
                    return False
            else:
                return False
            return True
```

# 2nd
方針：
1stの失敗を踏まえて，カッコ内部にカッコがあるパターンに対応するように修正．
具体的には，stack_list（リスト変数）を作成し，
 openカッコであればstackに追加
 そうでない場合はstack_listの末尾を確認し，対応するopenカッコがあればstack_listをpop
を繰り返す
最終的にstack_listが空であればTrueそうでなければFalseを返す

```python
class Solution:
    def isValid(self, s: str) -> bool:

        stack_list = []
        n_str = len(s)

        for i in range(n_str):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack_list.append(s[i])
            elif s[i] == ')' and stack_list != []:
                if stack_list[-1] != '(':
                    return False
                stack_list.pop()
            elif s[i] == '}' and stack_list != []:
                if stack_list[-1] != '{':
                    return False
                stack_list.pop()
            elif s[i] == ']' and stack_list != []:
                if stack_list[-1] != '[':
                    return False
                stack_list.pop()
            else:
                return False
        if stack_list != []:
            return False
        else:
            return True

```

# 3rd
方針：
if文が多いため分岐を削減して，RunTimeを短くする．
以下を参考にして，カッコのpairを辞書配列のキーと値で紐づけするようにした．
https://leetcode.com/problems/valid-parentheses/solutions/4850676/video-step-by-step-visualization-using-a-stack/

結果：
成功
Runtime 41ms -> 31ms

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []
        pairs = {"(": ")", "[": "]", "{": "}"}
        n_str = len(s)
        for bracket in s:
            if bracket in pairs:
                stack_list.append(bracket)
            else:
                if stack_list == [] or bracket != pairs[stack_list.pop()]:
                    return False
        if stack_list == []:
            return True
        else:
            return False
```

# 4th
方針：
小田さんのアドバイス通り，未使用の変数n_strを削除

結果：
成功
Runtime 41ms -> 31ms

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []
        pairs = {"(": ")", "[": "]", "{": "}"}
        for bracket in s:
            if bracket in pairs:
                stack_list.append(bracket)
            else:
                if stack_list == [] or bracket != pairs[stack_list.pop()]:
                    return False
        if stack_list == []:
            return True
        else:
            return False
```

# 5th
方針：
野田さんのアドバイスに基づいて2ndのコードを修正

結果：
成功
Runtime 38ms

```python
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
```

# 6th
方針：
野田さんのアドバイスに基づいて5thのコードを修正
if stack == []:をif not stack:に直す

結果：
成功
Runtime 26ms

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(',']':'[','}':'{'}
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack.pop() != pairs[ch]:
                    return False
        return not stack
```

# 7th 
Odaさんのコメントをもとにブラッシュアップ

``` Python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in '({[': # このほうが見やすい
                stack.append(ch)
                continue # early continue
            else:
                if not stack:
                    return False
                if stack.pop() != pairs[ch]:
                    return False
        return not stack
```

# 8th
Odaさんと野田さんのコメントを参考に修正
continue後のelseを消去
``` Python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in '({[': # このほうが見やすい
                stack.append(ch)
                continue # early continue
            if not stack:
                return False
            if stack.pop() != pairs[ch]:
                return False
        return not stack
```














