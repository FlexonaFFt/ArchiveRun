from collections import deque

def predictPartyVictory(senate: str) -> str:
    radiant = deque()
    dire = deque()
    
    for i, s in enumerate(senate):
        if s == 'R':
            radiant.append(i)
        else:
            dire.append(i)
    
    while radiant and dire:
        r = radiant.popleft()
        d = dire.popleft()
        
        if r < d:
            radiant.append(r + len(senate))
        else:
            dire.append(d + len(senate))
    return "Radiant" if radiant else "Dire"
# Runtime 11 ms, 79 %
# Memory 18.35, 16 %
print(predictPartyVictory("RD"))    # Output: "Radiant"
print(predictPartyVictory("RDD"))   # Output: "Dire"
