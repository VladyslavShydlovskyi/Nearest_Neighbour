import networkx as nx
import math
import matplotlib.pyplot as plt


def file_read(x):
    def wrapper(arr):
        if state == "f":
            x(arr)

    return wrapper


def keyboard_read(x):
    def wrapper(arr):
        if state == "k":
            x(arr)

    return wrapper


@keyboard_read
def keyboard(arr):
    print("Alright! Enter your coordinates line by line.")
    for i in range(number_of_nodes):
        line = input("Enter coords:")
        arr.append(line.split(" "))

    return arr


def file_in(arr):
    pass


def compute(coords, coords_clean):
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            tup = (i, j, round(math.sqrt((int(coords[i][0]) - int(coords[j][0])) ** 2
                                         + (int(coords[i][1]) - int(coords[j][1])) ** 2), 2))
            coords_clean.append(tup)
    return coords_clean


if __name__ == "__main__":
    state = input("Do you like to enter coords with a keyboard or file?""\n"
                  "Please enter \"f\" or \"k\"")
    number_of_nodes = int(input("How many nodes does your graph have?"))
    cities = nx.Graph()
    coordinates = []
    coordinates_clean = []
    keyboard(coordinates)
    file_in(coordinates)
    compute(coordinates, coordinates_clean)
    cities.add_weighted_edges_from(coordinates_clean)
    plt.subplot(121)
    nx.draw(cities, pos=nx.circular_layout(cities))
    plt.show()


