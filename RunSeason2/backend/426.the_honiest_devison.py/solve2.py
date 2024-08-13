from collections import Counter
from math import gcd
from functools import reduce

def max_substring(string):
    freq = Counter(string)
    counts = list(freq.values())
    overvall_gcd = reduce(gcd, counts)
    return overvall_gcd

if __name__ == '__main__':
    string = input().strip()
    print(max_substring(string))
