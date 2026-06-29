class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lights, prev = 0, 0
        for row in bank:
            devices = row.count("1")
            if devices: 
                lights += prev * devices
                prev = devices
        return lights
