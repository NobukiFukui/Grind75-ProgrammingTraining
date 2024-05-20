# ===============================================================
# (program) 13_ImplementQueueUsingStack
# WaveAlchemist
# Implement a first in first out (FIFO) queue using only two stacks. 
# The implemented queue should support all the functions of a normal 
# queue (push, peek, pop, and empty).
# URL: https://leetcode.com/problems/implement-queue-using-stacks/description/
# ===============================================================

#%%

class MyQueue:

    def __init__(self):
        # initiate instack and outstack as empty list
        self.instack, self.outstack = [], []

    def push(self, x: int) -> None:
        # append x at the end of instack
        self.instack.append(x)

    def pop(self) -> int:
        # exception
        if not self.outstack and not self.instack:
            raise Exception( "pop from empty list" )
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
#%%
myqueue = MyQueue()
# myqueue.push(1)
# myqueue.push(2)
# print(myqueue.peek())
print(myqueue.pop())
# print(myqueue.empty())

# %%
