class NumberContainer:

    def __init__(self):
        self.index_map = {}
        self.number_map = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_map:
            old_number = self.index_map[index]
            if old_number in self.number_map:
                if self.number_map[old_number] == {index}:
                    del self.number_map[old_number]
                else:
                    self.number_map[old_number].remove(index)

        self.index_map[index] = number
        if number in self.number_map:
            self.number_map[number].add(index)
        else:
            self.number_map[number] = {index}

    def find(self, number: int) -> int:
        if number in self.number_map:
            return min(self.number_map[number])
        return -1

# Решение не проходит 38 тест -> TL
def main():
    numberContainer = NumberContainer()
    numberContainer.change(1, 10)
    numberContainer.change(2, 20)
    numberContainer.change(1, 30)
    numberContainer.change(3, 10)
    findResult = numberContainer.find(10)
    print(findResult)

if __name__ == '__main__':
    main()
