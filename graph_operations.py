# This file helps user to generate graphs:
#
# input -> Give node counts,
# output-> and receive randomly connected graph
#
# uses networkx for graph representation,
# uses matplotlib for visual representation.

import random
import time

import networkx as nx


class GraphOperator:

    # This method creates a graph (from networkx lib).
    def __init__(self, node_count, intensity=0.75):
        # node count: node count is the node count that graph has. Every node has at least 1 neighbor.
        # intensity : probability of 2 nodes connection. Should be between 0.01 and 1.

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

        self.graph = graph
        self.node_count = node_count
        self.intensity = intensity

        if len(graph.nodes) > self.node_count:
            graph.remove_node(len(graph.nodes) - 1)
            print("Clearing node noise")

    # Assign a color to a node. Then, mark neighbors. Vertice is index integer!
    def assign_color_to_node(self, vertice, color):
        self.graph.nodes[vertice]["color"] = color

        # Update graph properties O(n)
        for neighbor in self.graph.neighbors(vertice):
            self.graph.nodes[neighbor]["colored_neighbor"] += 1

    # First missing positive problem, it is O(n), vertice is index integer!
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

    # MUST HAVE AT LEAST 1 COLORED NODE!
    def dsatur_Algorithm(self):

        start_time = time.time()
        # O(n) * (n + n + n) = O(3n^2)
        while True:

            # Use loop for each uncolored node. O(n)
            uncolored = []
            for i in range(0, self.node_count):
                if int(self.graph.nodes[i]["color"]) == 0:
                    uncolored.append(i)
            print(f"1 - Uncolored left: {len(uncolored)} {uncolored}")

            # If not left any uncolored nodes, it is finished!
            if len(uncolored) == 0:
                print("--- %s seconds ---" % (time.time() - start_time))
                print("Done algo!")
                return

            # Get all uncolored with neighbor colored. O(n)
            uncolored_with_colored_neighbor = []
            for i in uncolored:
                if int(self.graph.nodes[i]["colored_neighbor"] > 0):
                    uncolored_with_colored_neighbor.append(i)

            print(
                f"2 - Uncolored with colored neighbor: {len(uncolored_with_colored_neighbor)} {uncolored_with_colored_neighbor}")
            if len(uncolored_with_colored_neighbor) == 0:
                print("--- %s seconds ---" % (time.time() - start_time))
                print("Done algo!")
                return

            # Color all of them with assignable colors O(n).
            for i in uncolored_with_colored_neighbor:
                color_code = self.get_assignable_color_intensity(i)
                self.assign_color_to_node(i, color_code)
                print(f"Assigning to {i} color {color_code}")
