class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            conclude = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    res.append(j - i)
                    conclude = 1
                    break
            if conclude == 0:
                res.append(0)

        return res


        