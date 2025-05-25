#!/usr/bin/python3
"""an algorithm for the rain"""


def rain(walls):
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)
    total_water = 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[-1] = walls[-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    for i in range(1, n - 1):
        trapped = min(left_max[i], right_max[i]) - walls[i]
        if trapped > 0:
            total_water += trapped

    return total_water
