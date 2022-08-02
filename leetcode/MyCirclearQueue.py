'''
循环队列，实现对数据的循环利用。
神仙操作：
0 = rear = front的内容。可以很好的处理上
但判断有isFull（） == 》 有 rear%len = head
设计为rear+1%len = head！！
'''
class MyCircularQueue:

    def __init__(self, k: int):
        self.front = self.rear = 0
        self.elements = [0] * (k+1)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.elements[self.rear] = value
        self.rear = (self.rear + 1) % len(self.elements)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.elements)
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.elements[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.elements[(self.rear - 1) % len(self.elements)]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear + 1) % (len(self.elements)) == self.front