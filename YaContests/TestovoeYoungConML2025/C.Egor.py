def parse_availability(s):
    return [c == '.' for c in s]

c = int(input())
city_rooms = {}

for _ in range(c):
    parts, rooms = input().split(), []
    city, n = parts[0], int(parts[1])
    for _ in range(n):
        line = input().split()
        schedule, name = line[0], line[1]
        rooms.append((parse_availability(schedule), name))
    city_rooms[city] = rooms

m = int(input())
for _ in range(m):
    parts = input().split()
    l, cities, found = int(parts[0]), parts[1:], False
    rooms_lists = [city_rooms[city] for city in cities]
    for hour in range(24):
        current_rooms = []
        for rooms in rooms_lists:
            for schedule, name in rooms:
                if schedule[hour]:
                    current_rooms.append(name)
                    break
            else:
                break
        if len(current_rooms) == l:
            print("Yes", ' '.join(current_rooms))
            found = True
            break
    if not found:
        print("No")
