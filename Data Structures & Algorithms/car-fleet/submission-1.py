class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse = True)
        temp = 0
        count = 0
        for pos,spe in cars:
            time = (target-pos)/spe
            if time > temp:
                count += 1
                temp = time
        return count
