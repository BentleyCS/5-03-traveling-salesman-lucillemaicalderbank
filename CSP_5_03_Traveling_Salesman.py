import math
import itertools
import random


def getDistance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def getPathDistance(path):
    dist = 0
    for i in range(len(path)-1):
        dist += getDistance(path[i], path[i+1])
    return dist


def full_TSP(places):
    start = places[0]
    bestDist = float("inf")
    bestRoute = None

    for perm in itertools.permutations(places[1:]):  # fix start
        route = [start] + list(perm)
        d = getPathDistance(route)
        if d < bestDist:
            bestDist = d
            bestRoute = route

    return tuple(bestRoute)  # tuple required


def hueristic_TSP(places):
    path = [places.pop(0)]  # start at first city

    while places:
        current = path[-1]
        closest = places[0]
        closestDist = getDistance(current, closest)

        for city in places[1:]:
            d = getDistance(current, city)
            if d < closestDist:
                closestDist = d
                closest = city

        path.append(closest)
        places.remove(closest)

    return path


def generate_RandomCoordinates(n):
    return [[random.randint(10, 790), random.randint(10, 590)] for _ in range(n)]
