class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack, answer, prev = [], [0] * n, 0
        for command in logs:
            command_number, command_type, time_var = command.split(":")
            command, time = int(command_number), int(time_var)

            if command_type == 'start':
                if stack: answer[stack[-1]] += time - prev
                stack.append(command)
                prev = time

            else:
                top = stack.pop()
                answer[top] += time - prev + 1
                prev = time + 1

        return answer
