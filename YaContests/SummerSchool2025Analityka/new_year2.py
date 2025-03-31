from typing import List
import sys

class Solution:
    def solveFunction(self, n: int, nlst: List[str], m: int, mlst: List[str]) -> None:
        def time_to_seconds(time_str):
            hours, minutes, seconds = map(int, time_str.split(":"))
            return hours * 3600 + minutes * 60 + seconds

        electric_trains = []
        for i in range(n):
            train_id, departure_time, arrival_time, cost = nlst[i].split()
            electric_trains.append({
                "id": train_id,
                "departure": time_to_seconds(departure_time),
                "arrival": time_to_seconds(arrival_time),
                "cost": int(cost)
            })

        diesel_trains = []
        for i in range(m):
            data = mlst[i].split()
            train_id, departure_time, arrival_time = data[:3]
            diesel_trains.append({
                'id': train_id,
                'departure': time_to_seconds(departure_time),
                'arrival': time_to_seconds(arrival_time)
            })

        # Поиск оптимального маршрута
        best_route, min_cost = None, float("inf")
        for electric in electric_trains:
            for diesel in diesel_trains:
                if electric['arrival'] <= diesel['departure'] - 15 * 60:
                    total_cost = electric['cost']

                    if total_cost < min_cost or \
                       (total_cost == min_cost and diesel['arrival'] < best_route[1]['arrival']) or \
                       (total_cost == min_cost and diesel['arrival'] == best_route[1]['arrival'] and \
                        electric['departure'] < best_route[0]['departure']):
                        min_cost = total_cost
                        best_route = (electric, diesel)

        if best_route:
            print(f"Best Route: Electric {best_route[0]['id']} -> Diesel {best_route[1]['id']}, Cost: {min_cost}")
            print(best_route[0]['id'])
            print(best_route[1]['id'])


def test():
    solve = Solution()
    n, m = 3, 3
    nlist = ['6073 00:25:00 02:36:00 468',
        '083Y 06:05:05 07:58:59 1147',
        '7203 08:36:00 10:30:00 575']
    mlist = ['6731 10:05:00 11:24:00 246',
        'ABCDE 02:50:59 03:15:00 100',
        'X 02:51:00 03:25:00 200']

    nlist2 = ["QT 03:33:22 13:34:29 300",
        "6OD 08:53:02 09:07:32 300",
        "17X6M 07:35:48 18:56:54 300"]
    mlist2 = ['A1E 03:47:30 05:54:32 300',
        '61FU2 08:34:44 15:19:11 300',
        'SOJ7K 08:52:25 22:45:04 300']

    solve.solveFunction(n, nlist, m, mlist)
    solve.solveFunction(n, nlist2, m, mlist2)


def main():
    solve = Solution()
    nlist, mlist = [], []

    n = int(input())
    for _ in range(n):
        ndata = input().strip()
        nlist.append(ndata)

    m = int(input())
    for _ in range(m):
        mdata = input().strip()
        mlist.append(mdata)

    solve.solveFunction(n, nlist, m, mlist)


if __name__ == '__main__':
    main()
