class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        minStack = []
        temp_index = dict()
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if temp not in temp_index:
                temp_index[temp] = []
            temp_index[temp].append(i)
            while len(minStack) > 0 and minStack[-1] < temp:
                lower_index = temp_index[minStack[-1]].pop()
                res[lower_index] = i - lower_index
                minStack.pop()
            minStack.append(temp)
        
        return res