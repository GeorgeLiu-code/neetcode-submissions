class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse = True)
        count = 0
        temp = 0

        for i in cars:
            time = (target - i[0])/i[1]
            if time > temp:
                count += 1
                temp = time
        return count

