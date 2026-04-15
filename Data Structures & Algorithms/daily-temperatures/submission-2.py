class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # maintain list in a monotonically increasing order
        min_temp_index = []
        results = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if len(min_temp_index) == 0:
                min_temp_index.append([i, temp])
            else:
                while len(min_temp_index) and temp > min_temp_index[-1][1]:
                    results[min_temp_index[-1][0]] = i - min_temp_index[-1][0]
                    min_temp_index.pop()
                min_temp_index.append([i, temp])
        
        return results