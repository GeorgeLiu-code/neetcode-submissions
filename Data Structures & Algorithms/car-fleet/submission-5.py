class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)):
            stack.append((position[i],speed[i]))
        stack = sorted(stack,reverse = True)
        
        time = []
        fleet = 0
        temp = 0
        for j in range(len(position)):
            time.append((target-stack[j][0]) / stack[j][1]) 
            if temp < time[j]: # compare last fleet's time not last car
                fleet += 1
                temp = time[j]
        return fleet
        