class MyQueue:

    def __init__(self):
        self._in: list[int] = []
        self._out: list[int] = []

    def push(self, x: int) -> None:
        self._in.append(x)

    def _move_if_needed(self) -> None:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
    
    def pop(self) -> int:
        self._move_if_needed()
        return self._out.pop()

    def peek(self) -> int:
        self._move_if_needed()
        return self._out[-1]

    def empty(self) -> bool:
        return not self._in and not self._out
