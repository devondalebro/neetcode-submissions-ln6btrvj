class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeed = []
        for i in range(len(position)):
            positionSpeed.append((position[i], speed[i]))
        positionSpeed.sort(reverse=True)
        stack = []
        fleets = 0
        for p, s in positionSpeed:
            time = (target - p) / s
            if len(stack) == 0:
                fleets += 1
                stack.append(time)
                print("1")
            elif time <= stack[-1]:
                print("2")
            else:
                print("3")
                stack.pop()
                fleets += 1
                stack.append(time)
        
        return fleets
