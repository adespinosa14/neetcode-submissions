class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            s_struct = [t, i]
            while stack and t > stack[-1][0]:
                val = stack.pop()
                print(f"{i} - {val}")
                res[val[1]] = i - val[1]
            stack.append(s_struct)

        return res