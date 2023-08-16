import math
import random


def randlatlon2r():
    pi = math.pi
    angle = 0
    i = 0
    ArreyResult = []

    while i < 359:
        angleRadian = angle * pi / 180
        lat = math.sin(angleRadian) + 0.3 * math.cos(angleRadian * 8) + \
            0.1 * math.sin(angleRadian * 25) + 0.3 * math.cos(angleRadian * 12)
        lon = angleRadian
        speed = random.randint(1, 90)
        ArreyResult.append({'long': lon * 180 / pi, 'lat': lat * 180 / pi, 'speed': speed})
        i +=1
        angle += 1
    return ArreyResult



