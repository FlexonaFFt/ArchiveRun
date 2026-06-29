from sortedcontainers import SortedList

# Runtime 308 ms, 32.84 %
# Memory 95.24 mb, 37.85 %
class NumberContainer:
    def __init__(self):
        self.index_map = {}
        self.number_map = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_map:
            old_number = self.index_map[index]
            self.number_map[old_number].remove(index)
            if not self.number_map[old_number]:
                del self.number_map[old_number]

        self.index_map[index] = number
        if number not in self.number_map:
            self.number_map[number] = SortedList()
        self.number_map[number].add(index)

    def find(self, number: int) -> int:
        if number in self.number_map and self.number_map[number]:
            return self.number_map[number][0]
        return -1
