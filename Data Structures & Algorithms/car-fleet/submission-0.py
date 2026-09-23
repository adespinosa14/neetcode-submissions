class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[s,p] for s, p in zip(position, speed)]
        fleet = sorted(pairs, reverse=True)

        stack = []
        for p,s in fleet:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        print(stack)
        return len(stack)