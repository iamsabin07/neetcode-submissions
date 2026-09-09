class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        signs = ["+","-","*","/"]
        for i in tokens:
            if i not in signs:
                stack.append(int(i))
            else:
                if i == "+":
                    res = stack.pop() + stack.pop()
                    stack.append(res)
                elif i == "*":
                    res = stack.pop() * stack.pop()
                    stack.append(res)
                elif i == "-":
                    temp = stack.pop()
                    temp2 = stack.pop()
                    res = temp2-temp
                    stack.append(res)
                else:
                    temp = stack.pop()
                    temp2 = stack.pop()
                    res = int(temp2 / temp)
                    stack.append(res)
        
        return stack.pop()

        