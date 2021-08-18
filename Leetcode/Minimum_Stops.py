from heapq import heappop, heappush, heapify


def heappop_max(heap):
    return -heappop(heap)


def heappush_max(heap, value):
    return heappush(heap, -value)


def min_refuel_stops(target: int, start_fuel: int, stations: [[int]]) -> int:
    heap_max = []
    heapify(heap_max)
    i = 0
    res = 0
    while start_fuel < target:
        while i < len(stations) and stations[i][0] <= start_fuel:
            heappush_max(heap_max, stations[i][1])
            i += 1
        if len(heap_max) == 0:
            return -1
        start_fuel += heappop_max(heap_max)
        res += 1
    return res


if __name__ == '__main__':
    print(min_refuel_stops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]))
