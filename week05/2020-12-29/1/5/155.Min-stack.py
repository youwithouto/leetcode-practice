# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.elements = [0]

    def push(self, x: int) -> None:
        elementIndex = len(self.elements)
        self.elements.append(x)
        parentIndex = elementIndex // 2
        while parentIndex > 0 and self.elements[parentIndex] > x:
            self.elements[elementIndex] = self.elements[parentIndex]
            elementIndex, parentIndex = parentIndex, parentIndex // 2
        self.elements[elementIndex] = x

    def pop(self) -> None:
        lastEelementValue = self.elements.pop()
        elementIndex = 1
        childIndex = 2 * elementIndex
        while childIndex <= len(self.elements) - 1:
            if childIndex + 1 < len(self.elements) and self.elements[childIndex + 1] < self.elements[childIndex]:
                childIndex += 1
            if lastEelementValue > self.elements[childIndex]:
                self.elements[elementIndex] = self.elements[childIndex]
                elementIndex, childIndex = childIndex, 2 * childIndex
            else:
                break
        self.elements[elementIndex] = lastEelementValue

    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        return self.elements[1]
