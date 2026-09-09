class MinStack:

    def __init__(self):
        self.arr = []
        self.minArr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if(len(self.minArr) == 0):
            self.minArr.append(val)
        else:
            temp = self.minArr[-1]
            if(temp > val):
                self.minArr.append(val)
            else:
                self.minArr.append(temp)

    def pop(self) -> None:
        self.arr.pop()
        self.minArr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minArr[-1]
