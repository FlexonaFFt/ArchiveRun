class MySolution:

    def func(self, data):
        return len(set(data))

    def main(self):
        data = __import__("sys").stdin.read().split()
        print(self.func(data))


if __name__ == '__main__':
    MySolution().main()