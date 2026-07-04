"""
AAABBCCCCCCDB -> 3A2B6CDB
"""

class Solution:
    def main(self, string: str) -> str: 
        result, counter = [], 0 

        for i in range(1, len(string)):
            if string[i] == string[i - 1]: counter += 1
            else: 
                if counter > 1: result.append(str(counter) + string[i - 1])
                else: result.append(string[i - 1])
                counter = 1 

        # Важно не забыть последнюю группу
        if counter > 1: result.append(str(counter) + string[-1])
        else: result.append(string[-1])
        return ''.join(result)


if __name__ == '__main__':
    strng = "AAABBCCCCCCDB"
    print(Solution().main(strng))
