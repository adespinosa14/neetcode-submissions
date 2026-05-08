class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    val = stack.pop()
                    val_two = stack.pop()
                    stack.append(val_two - val)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    val = stack.pop()
                    val_two = stack.pop()
                    stack.append(int(val_two / val))
                case _:
                    stack.append(int(token)) 
        return stack[0]
        