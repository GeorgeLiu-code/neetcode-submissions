class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse = True)
        prevTime = (target - cars[0][0]) / cars[0][1]
        temp = 0
        count = 1
        for i in range(1,len(cars)):
            currTime = (target - cars[i][0]) / cars[i][1]
            if currTime > prevTime:
                count += 1
                prevTime = currTime
        return count



        