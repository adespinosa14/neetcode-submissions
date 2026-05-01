class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1: return False
        stack = []

        for b in s:
            print(stack)
            match b:
                case '}':
                    val = stack.pop() if len(stack) > 0 else None
                    if val == None or val != '{': return False

                case ')':
                    val = stack.pop() if len(stack) > 0 else None
                    if val == None or val != '(': return False
                case ']':
                    val = stack.pop() if len(stack) > 0 else None
                    if val == None or val != '[': return False
                case _:
                    stack.append(b)

        return True if len(stack) == 0 else False
                

        