# 13_ImplementQueueUsingStack
Author: WaveAlchemist  
URL:https://leetcode.com/problems/implement-queue-using-stacks/

# 1st 
入力用出力用それぞれについてstackを用意
pushではinstackとなるリストにappendを適用
peekではinstackの各要素をoutstackに逆向きに追加し，outstackの末尾を返す
popはpeekを呼び出した後にoutstackの先頭をpopする
emptyはinstackとoutstackが空になっていないかをチェック
参考：
https://qiita.com/mhiro216/items/adc892ede78eec06ef96

実行時間：29ms, メモリ：16.59MB

``` Python
class MyQueue:

    def __init__(self):
        # initiate instack and outstack as empty list
        self.instack, self.outstack = [], []

    def push(self, x: int) -> None:
        # append x at the end of instack
        self.instack.append(x)

    def pop(self) -> int:
        # call peek
        self.peek()
        # return deleted element by pop
        return self.outstack.pop()

    def peek(self) -> int:
        # if outstack is empty, the elements in instack are moved into outstack
        if not self.outstack:
            while self.instack:
                self.outstack.append( self.instack.pop() )
        # return the end element of outstack
        return self.outstack[-1]

    def empty(self) -> bool:
        return not self.instack and not self.outstack
```