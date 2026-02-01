import math
import random
import pygame
import itertools


def getDistance(spot1, spot2):
    # Given two coordinates in a plane return the distance between those two points.
    return math.sqrt(
        (spot1[0] - spot2[0]) ** 2 +
        (spot1[1] - spot2[1]) ** 2
    )


def getPathDistance(places: list):
    # Distance to visit all places in order and return to start
    dist = 0
    for i in range(len(places) - 1):
        dist += getDistance(places[i], places[i + 1])
    dist += getDistance(places[-1], places[0])
    return dist


def generatePermutations(places: list):
    return list(itertools.permutations(places))


def full_TSP(places: list):
    bestRoute = None
    bestDist = float("inf")
    calculations = 0

    for perm in generatePermutations(places):
        calculations += 1
        d = getPathDistance(list(perm))
        if d < bestDist:
            bestDist = d
            bestRoute = list(perm)

    print(f"there were {calculations} calculations for full TSP")
    return bestRoute


def hueristic_TSP(places: list):
    calculations = 0
    path = [places.pop(0)]

    while places:
        current = path[-1]
        closest = None
        closestDist = float("inf")

        for spot in places:
            calculations += 1
            d = getDistance(current, spot)
            if d < closestDist:
                closestDist = d
                closest = spot

        path.append(closest)
        places.remove(closest)

    print(f"there were {calculations} calculations for hueristic TSP")
    return path


def generate_RandomCoordinates(n):
    newPlaces = []
    for _ in range(n):
        newPlaces.append([random.randint(10, 790), random.randint(10, 590)])
    return newPlaces


places = [[80, 75], [100, 520], [530, 300], [280, 200],
          [350, 150], [700, 120], [400, 500]]


def DrawExample(places):
    TSP = full_TSP(places.copy())
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

        # Full TSP (red)
        for i in range(len(TSP) - 1):
            pygame.draw.line(screen, (255, 0, 0), TSP[i], TSP[i + 1], 8)
        if TSP:
            pygame.draw.line(screen, (255, 0, 0), TSP[0], TSP[-1], 8)

        # Heuristic (blue)
        for i in range(len(Hueristic) - 1):
            pygame.draw.line(screen, (0, 0, 255), Hueristic[i], Hueristic[i + 1], 4)
        if Hueristic:
            pygame.draw.line(screen, (0, 0, 255), Hueristic[0], Hueristic[-1], 4)

        # Cities
        for spot in places:
            pygame.draw.circle(screen, (0, 0, 0), spot, 10)

        text = font.render("Red = Full TSP | Blue = Heuristic", True, (0, 0, 0))
        screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()


DrawExample(places)
