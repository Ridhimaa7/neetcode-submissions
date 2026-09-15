class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                new_temp, new_index = stack.pop()
                output[new_index] = abs(new_index - index)
            stack.append([temp,index])
        return output