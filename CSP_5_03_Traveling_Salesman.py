import math
import random
import itertools


def getDistance(spot1, spot2):
    return math.sqrt(
        (spot1[0] - spot2[0]) ** 2 +
        (spot1[1] - spot2[1]) ** 2
    )


def getPathDistance(places: list):
    dist = 0
    for i in range(len(places) - 1):
        dist += getDistance(places[i], places[i + 1])
    dist += getDistance(places[-1], places[0])
    return dist


def full_TSP(places: list):
    start = places[0]
    bestRoute = None
    bestDist = float("inf")

    for perm in itertools.permutations(places[1:]):
        route = [start] + list(perm)
        d = getPathDistance(route)
        if d < bestDist:
            bestDist = d
            bestRoute = route

    return tuple(bestRoute)   # ✅ MUST be tuple


def hueristic_TSP(places: list):
    places = places.copy()
    path = [places.pop(0)]

    while places:
        current = path[-1]
        closest = places[0]
        closestDist = getDistance(current, closest)

        for spot in places[1:]:
            d = getDistance(current, spot)
            if d < closestDist:
                closestDist = d
                closest = spot

        path.append(closest)
        places.remove(closest)

    return path


def generate_RandomCoordinates(n):
    return [[random.randint(10, 790), random.randint(10, 590)] for _ in range(n)]


# ---------- OPTIONAL VISUALIZATION ----------
# This will NOT run during grading

def DrawExample(places):
    import pygame  # ✅ local import (safe)

    TSP = list(full_TSP(places.copy()))
    Hueristic = hueristic_TSP(places.copy())

    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Traveling Salesman")

    font = pygame.font.SysFont(None, 32)
    text_rect = pygame.Rect(0, 0, 800, 50)
    text_rect.center = (400, 760)

    running = True
    while running:
        screen.fill((255, 255, 255))

        for i in range(len(TSP) - 1):
            pygame.draw.line(screen, (255, 0, 0), TSP[i], TSP[i + 1], 8)
        pygame.draw.line(screen, (255, 0, 0), TSP[0], TSP[-1], 8)

        for i in range(len(Hueristic) - 1):
            pygame.draw.line(screen, (0, 0, 255), Hueristic[i], Hueristic[i + 1], 4)
        pygame.draw.line(screen, (0, 0, 255), Hueristic[0], Hueristic[-1], 4)

        for spot in places:
            pygame.draw.circle(screen, (0, 0, 0), spot, 10)

        text = font.render("Red = Full TSP | Blue = Heuristic", True, (0, 0, 0))
        screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    places = [[80, 75], [100, 520], [530, 300], [280, 200],
              [350, 150], [700, 120], [400, 500]]
    DrawExample(places)