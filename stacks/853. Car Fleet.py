class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse = True)
        merge_check = -1
        fleets = 0

        for pos, spd in cars:

            time_to_target = (target - pos) / spd

            if time_to_target > merge_check:
                merge_check = time_to_target
                fleets += 1

        return fleets