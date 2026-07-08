class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            l = 0
            for j in range(i+1, len(temperatures)):
                l += 1
                if temperatures[j] > temperatures[i]:
                    res[i] = l
                    break
        res[i] = l
        return res