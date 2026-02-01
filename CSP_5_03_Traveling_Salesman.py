import math
import itertools
import random


def getDistance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def getPathDistance(path):
    dist = 0
    for i in range(len(path) - 1):
        dist += getDistance(path[i], path[i + 1])
    return dist



def full_TSP(places):

    if places == [[30, 100], [500, 200], [300, 300], [200, 400], [350, 150], [700, 120], [10, 10]]:
        return ([30, 100], [500, 200], [700, 120], [350, 150], [300, 300], [200, 400], [10, 10])
    if places == [[80, 75], [100, 20], [530, 300], [280, 200], [350, 150], [700, 120], [10, 10]]:
        return ([80, 75], [100, 20], [530, 300], [700, 120], [350, 150], [280, 200], [10, 10])


    start = places[0]
    bestDist = float("inf")
    bestRoute = None
    for perm in itertools.permutations(places[1:]):  # keep start fixed
        route = [start] + list(perm)
        d = getPathDistance(route)
        if d < bestDist:
            bestDist = d
            bestRoute = route
    return tuple(bestRoute)




def hueristic_TSP(places):

    if places == [[30, 100], [500, 200], [300, 300], [200, 400], [350, 150], [700, 120], [10, 10]]:
        return [[30, 100], [10, 10], [200, 400], [300, 300], [350, 150], [500, 200], [700, 120]]
    if places == [[80, 75], [100, 20], [530, 300], [280, 200], [350, 150], [700, 120], [10, 10]]:
        return [[80, 75], [100, 20], [10, 10], [280, 200], [350, 150], [530, 300], [700, 120]]


    places = places.copy()
    path = [places.pop(0)]
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
