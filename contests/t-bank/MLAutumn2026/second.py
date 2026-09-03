import sys
from collections import Counter

data = sys.stdin.buffer.read().split()
cnt = Counter(data[1:])

best = max(cnt.values())
answer = sorted(s for s, count in cnt.items() if count == best)
sys.stdout.buffer.write(b'\n'.join(answer))
