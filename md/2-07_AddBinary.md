# 2-07 AddBinary
Author: WaveAlchemist
URL:https://leetcode.com/problems/add-binary/description/

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

# 1st 
２進数の筆算をイメージしてコードに落とし込んだ，
繰上り無の時
k桁目の足し算 0 + 0 -> 0; 1 + 0 -> 1; 1 + 1 -> 0 k+1桁目繰上り
繰上りの時
k桁目の足し算 0 + 0 -> 1; 1 + 0 -> 0; 1 + 1 -> 1 k+1桁目繰上り
abの桁数が違うときにどう処理するかでかなり悩んでしまい，40分ほど時間がかかってしまった
結局，aとbの小さい方を0でパディングすることで解決した
``` Python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # initialize sum result
        result = ""
        flag_increase_digit = 0
        # binary length
        length_binary = max(len(a), len(b)) + 1
        # zero padding
        a = "0" * (length_binary - len(a)) + a
        b = "0" * (length_binary - len(b)) + b

        # check every digit
        for i in range( -1, -length_binary - 1, -1 ):
            if flag_increase_digit == 0: # case of NO increse of digit
                if a[i] == "1" and b[i] == "1":
                    result = "0" + result
                    flag_increase_digit = 1
                elif a[i] == "0" and b[i] == "0":
                    result = "0" + result
                    flag_increase_digit = 0
                else:
                    result = "1" + result
                    flag_increase_digit = 0
            else:                        # case of increse of digit
                if a[i] == "1" and b[i] == "1":
                    result = "1" + result
                    flag_increase_digit = 1
                elif a[i] == "0" and b[i] == "0":
                    result = "1" + result
                    flag_increase_digit = 0
                else:
                    result = "0" + result
                    flag_increase_digit = 1     
        if result[0] == "0":            # remove padded "0"
            result = result[1:]
        return result
```

# 2nd
discord内では解いている人がいないため，leetcode上でほかの例を参考にした
https://leetcode.com/problems/add-binary/solutions/1679423/well-detailed-explaination-java-c-python-easy-for-mind-to-accept-it/

while i>=0 or j>=0の条件にしておけばzero paddingの必要はなくなる


``` Python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # initialize result, pointer and carry
        result = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        # calculate binary sum
        while i >= 0 or j >= 0:
            sum = carry
            # check each digit
            if i >= 0:
                sum += ord(a[i]) - ord("0")
            if j >= 0:
                sum += ord(b[j]) - ord("0")
            # proceed pointer
            i, j = i - 1, j - 1
            if sum >= 2:
                carry = 1
            else:
                carry = 0
            # check result
            # result = 0 -> carry = 0
            # result = 1 -> carry = 0
            # result = 2 -> carry = 1
            # result = 3 -> carry = 1
            result = str(sum % 2) + result
        # check carry at largest digit
        if carry == 1:
            result = str(carry) + result
        return result
```

# 3rd
レビューコメントをもとに以下を修正
・i, jの名前をpointer_a, pointer_bに
・文字列の結合には+=を利用し，最後にresultを逆順にして返す
・carryのチェックでif文ではなくtotal // 2を利用

``` Python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # initialization
        result = ""
        pointer_a, pointer_b = len(a) - 1, len(b) - 1
        carry = 0
        # calculate binary sum
        while pointer_a >= 0 or pointer_b >= 0:
            total = carry
            # check each digit
            if pointer_a >= 0:
                total += ord(a[pointer_a]) - ord("0")
            if pointer_b >= 0:
                total += ord(b[pointer_b]) - ord("0")
            # proceed pointers
            pointer_a -= 1
            pointer_b -= 1
            # check carrying forward
            carry = total // 2
            # check result
            result += str(total % 2)
        # check carrying forward at largest digit
        if carry == 1:
            result += str(carry)
        return result[::-1] # reverse digits
```

+= を使わずにlistにbinaryを入れて後でresultに結合という方法も用いたが，
前者のほうが計算速度は速そう

``` Python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # initialization 
        result_list = []
        pointer_a, pointer_b = len(a) - 1, len(b) - 1
        carry = 0
        # main loop for calculation of binary sum
        while pointer_a >= 0 or pointer_b >= 0:
            # total sum of carry forward
            total = carry
            # check each digit
            if pointer_a >= 0:
                total += ord(a[pointer_a]) - ord("0")
            if pointer_b >= 0:
                total += ord(b[pointer_b]) - ord("0")
            # proceed pointers
            pointer_a -= 1
            pointer_b -= 1
            # check carry forward
            #  total = 0 -> carry = 0, result = "0"
            #  total = 1 -> carry = 0, result = "1"
            #  total = 2 -> carry = 1, result = "0"
            #  total = 3 -> carry = 1, result = "1"
            carry = total // 2            
            # append result binary
            result_list.append(str(total % 2))
        # check carrying forward at largest digit
        if carry == 1:
            result_list.append(str(carry))
        result = "".join(result_list)
        return result[::-1]
```