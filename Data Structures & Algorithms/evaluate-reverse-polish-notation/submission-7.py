class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for token in tokens:
            match token:
                case '+':
                    val = stack.pop()
                    val_two = stack.pop()
                    res = val_two + val
                    stack.append(res)
                case '-':
                    val = stack.pop()
                    val_two = stack.pop()
                    res = val_two - val
                    stack.append(res)
                case '*':
                    val = stack.pop()
                    val_two = stack.pop()
                    res = val * val_two
                    stack.append(res)
                case '/':
                    val = stack.pop()
                    val_two = stack.pop()
                    res = val_two / val
                    stack.append(int(res))
                case _:
                    stack.append(int(token)) 
        return stack[0]
        