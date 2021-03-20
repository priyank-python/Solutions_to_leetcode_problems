'''
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:

MaxStack() Initializes the stack object.
void push(int x) Pushes element x onto the stack.
int pop() Removes the element on top of the stack and returns it.
int top() Gets the element on the top of the stack without removing it.
int peekMax() Retrieves the maximum element in the stack without removing it.
int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.
 

Example 1:

Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
stk.top();     // return 5, [5] the stack did not change.
 

Constraints:

-107 <= x <= 107
At most 104 calls will be made to push, pop, top, peekMax, and popMax.
There will be at least one element in the stack when pop, top, peekMax, or popMax is called.
 '''

 class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        item = self.stack[len(self.stack)-1]
        self.stack = self.stack [:len(self.stack)-1]
        return (item)

    def top(self):
        """
        :rtype: int
        """
        return (self.stack[len(self.stack)-1])

    def peekMax(self):
        """
        :rtype: int
        """
        maximum = self.stack[0]
        for item in self.stack[1:]:
            if item > maximum:
                maximum = item
        return (maximum)

    def popMax(self):
        """
        :rtype: int
        """
        maximum = self.stack[0]
        for item in self.stack[1:]:
            if item > maximum:
                maximum = item
        indices_max = []
        for index in range (0,len(self.stack)):
            if self.stack[index] == maximum:
                indices_max.append (index)
        index_removal = max (indices_max)
        stack2 = []
        for index in range (0,len(self.stack)):
            if index != index_removal:
                stack2.append (self.stack[index])
        self.stack = stack2
        return (maximum)    


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()