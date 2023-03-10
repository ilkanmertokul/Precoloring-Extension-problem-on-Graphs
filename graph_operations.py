# İlkan Mert Okul,
# ilkan.okul2018@gtu.edu.tr
# 1801042649

# This class is helper class for using networkx graphs.

import random
import time
import networkx as nx
import csv


# GraphOperator class as a wrapper class for networkx graph.
# It can create graphs
# - randomly -> Give node count (int) and intensity (int)
# - from file. -> Give file path (string)
class GraphOperator:

    # Constructor that saves the parameters for class properties.
    # graph : graph for the GraphOperator.
    # node_count : node count for graph.
    def __init__(self, graph, node_count):

        print("Successfully created the graph!")
        self.graph = graph
        self.node_count = node_count
        self.time = -1

        # Creating graph can sometimes create a noise while trying to stay at 1 piece. This clears it.
        if len(graph.nodes) > self.node_count:
            graph.remove_node(len(graph.nodes) - 1)
            print("Clearing node noise")

    # This function passes its parameter to the constructor.
    # filename : path to the file to read.
    @classmethod
    def from_filename(cls, filename):

        graph = nx.Graph()
        node_count = 0

        with open(filename, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

            i = 0
            for row in spamreader:

                node_count = len(row)
                # First row, get colors.
                if i == 0:
                    for j in range(0, node_count):
                        graph.add_node(j, color=int(row[j]), colored_neighbor=0)
                else:
                    for j in range(i, node_count):
                        if int(row[j]) == 1:
                            graph.add_edge(i - 1, j)
                            print(f"edge {i - 1} to {j}")
                i += 1

            # Update neighbors for colored nodes.
            for i in range(node_count):
                if graph.nodes[i]["color"] != 0:
                    for neighbor in graph.neighbors(i):
                        graph.nodes[neighbor]["colored_neighbor"] += 1

        return cls(graph, node_count)

    # This function passes its parameter to the constructor.
    # node count: node count is the node count that graph has. Every node has at least 1 neighbor.
    # intensity : probability of 2 nodes connection. Should be between 0.01 and 1.
    @classmethod
    def from_random_generator(cls, node_count, intensity=0.75):

        if intensity > 1 or intensity < 0.001:
            print("Invalid graph intensity. Defaulting back to 0.25")
            intensity = 0.25
        print(f" Creating {node_count} node graph with intensity of {intensity}.")
        graph = nx.Graph()

        # 1-Initialize nodes
        for i in range(0, node_count):
            graph.add_node(i, color=0, colored_neighbor=0)
            print(f" Created node: {graph.nodes[i]}")
        print("done")

        # 2-Initialize edges
        intensity *= 100
        for i in range(0, node_count):
            connected = False
            for j in range(i + 1, node_count):
                if random.randint(0, 99) < intensity:
                    graph.add_edge(i, j)
                    connected = True
            if not connected:
                j = i
                while j == i:
                    j = random.randint(0, node_count)
                graph.add_edge(i, j)

        return cls(graph, node_count)

    # Assign a color to a node. Then, mark neighbors.
    # vertice : index of graph node, int.
    # color : color to give, int, positive.
    def assign_color_to_node(self, vertice, color):
        self.graph.nodes[vertice]["color"] = color

        # Update graph properties O(n)
        for neighbor in self.graph.neighbors(vertice):
            self.graph.nodes[neighbor]["colored_neighbor"] += 1

    # First missing positive problem, it is O(n)
    # vertice : index of graph node, int.
    def get_assignable_color_intensity(self, vertice):

        # Get all neighbours color intensity to array.
        neighbors = self.graph.neighbors(vertice)
        colors = []
        for neighbor in neighbors:
            colors.append(self.graph.nodes[neighbor]["color"])

        m = max(colors)  # Storing maximum value
        if m < 1:
            # In case all values in our array are negative
            return 1
        if len(colors) == 1:
            # If it contains only one element
            return 2 if colors[0] == 1 else 1
        q = [0] * m

        for i in range(len(colors)):
            if colors[i] > 0:
                if q[colors[i] - 1] != 1:
                    # Changing the value status at the index of our list
                    q[colors[i] - 1] = 1

        for i in range(len(q)):
            # Encountering first 0, i.e, the element with the least value
            if q[i] == 0:
                return i + 1
                # In case all values are filled between 1 and m

        return i + 2

    # Dsatur algorithm for partial colored graphs.
    def dsatur_Algorithm(self):

        start_time = time.time()
        # O(n) * (n + n + n) = O(n^2)
        while True:

            # Use loop for each uncolored node. O(n)
            uncolored = []
            for i in range(0, self.node_count):
                if int(self.graph.nodes[i]["color"]) == 0:
                    uncolored.append(i)
            print(f"1 - Uncolored left: {len(uncolored)} {uncolored}")

            # If not left any uncolored nodes, it is finished!
            if len(uncolored) == 0:
                break

            # Get all uncolored with neighbor colored. O(n)
            uncolored_with_colored_neighbor = []
            for i in uncolored:
                if int(self.graph.nodes[i]["colored_neighbor"] > 0):
                    uncolored_with_colored_neighbor.append(i)

            print(f"2 - Uncolored with colored neighbor: "
                  f"{len(uncolored_with_colored_neighbor)} {uncolored_with_colored_neighbor}")
            if len(uncolored_with_colored_neighbor) == 0:
                break

            # Color all of them with assignable colors O(n^2).
            for i in uncolored_with_colored_neighbor:
                color_code = self.get_assignable_color_intensity(i)
                self.assign_color_to_node(i, color_code)
                print(f"Assigning to {i} color {color_code}")

        self.get_max_color_after_algorithm()
        self.time = time.time() - start_time
        print("--- %s seconds ---" % (time.time() - start_time))
        print("Done algo!")
        return

    # Return max color intensity that is assigned to nodes. O(n)
    def get_max_color_after_algorithm(self):

        max_color = -1
        for i in range(0, self.node_count):
            if max_color < self.graph.nodes[i]["color"]:
                max_color = self.graph.nodes[i]["color"]

        print(f"Max color is : {max_color}")
        return max_color

    def get_time(self):
        return self.time
