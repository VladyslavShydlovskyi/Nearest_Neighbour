import networkx as nx
import math
import matplotlib.pyplot as plt


def keyboard(arr):
    print("Alright! Enter your coordinates line by line.")
    for i in range(number_of_nodes):
        line = input("Enter coords:")
        arr.append(line.split(" "))

    return arr


def compute(coords, coords_clean):
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            tup = (i, j, round(math.sqrt((int(coords[i][0]) - int(coords[j][0])) ** 2
                                         + (int(coords[i][1]) - int(coords[j][1])) ** 2), 2))

            tup2 = (j, i, round(math.sqrt((int(coords[i][0]) - int(coords[j][0])) ** 2
                                          + (int(coords[i][1]) - int(coords[j][1])) ** 2), 2))
            coords_clean.append(tup)
            coords_clean.append(tup2)
    return coords_clean


def min_distance(clean_coords, startt):
    init_start = startt
    minn = float('inf')
    used_starts = []
    length = len(clean_coords)
    distance = 0
    temp = []
    temp_dots = []
    clean = []
    for i in range(length - number_of_nodes):
        for j in range(length):
            cur_dot = clean_coords[j][0]
            if cur_dot == startt and (clean_coords[j][1] not in used_starts) and (cur_dot not in used_starts):
                cur_min = clean_coords[j][2]
                if minn > cur_min:
                    minn = cur_min
                    temp_dots = [clean_coords[j][0], clean_coords[j][1]]

        distance += minn if minn != float('inf') else 0
        minn = float('inf')
        temp.append(temp_dots)
        used_starts.append(startt)
        startt = temp[i][1]

    temp.pop(len(temp) - 1)
    for i in range(length):
        x = clean_coords[i][0]
        y = clean_coords[i][1]
        if x == startt and y == init_start:
            temp.append([startt, init_start])
            distance += clean_coords[i][2]

    for i in range(len(temp)):
        if temp[i] not in clean:
            clean.append(temp[i])


    print(clean)
    print(distance)


if __name__ == "__main__":
    number_of_nodes = int(input("How many nodes does your graph have? "))
    coordinates = []
    coordinates_clean = []
    keyboard(coordinates)
    compute(coordinates, coordinates_clean)
    start = int(input("Enter your start point(number from 0 to %d) " % (number_of_nodes - 1)))
    min_distance(coordinates_clean, start)
