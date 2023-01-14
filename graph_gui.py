import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk
import networkx as nx
import random

import graph_operations
import graph_painter


class GraphGraphicalInterface:

    def __init__(self):
        self.root = tk.Tk()

        self.b3 = tk.Button(self.root, text="Run precoloring algorithm", command=self.run_algorithm)
        self.b3.pack(side='right')

        self.b1 = tk.Button(self.root, text="Build a random graph", command=self.build_graph_randomly)
        self.b1.pack(side='bottom')

        self.e1 = tk.Entry(self.root)
        self.e1.insert(0, 'Intensity')
        self.e1.pack(side='bottom')

        self.e2 = tk.Entry(self.root)
        self.e2.insert(0, 'NodeCount')
        self.e2.pack(side='bottom')

        self.e4 = tk.Entry(self.root)
        self.e4.insert(0, 'Precolored nodes')
        self.e4.pack(side='bottom')

        self.b2 = tk.Button(self.root, text="Build from filename", command=self.build_graph_from_file)
        self.b2.pack(side='left')

        self.e3 = tk.Entry(self.root)
        self.e3.insert(0, 'filename')
        self.e3.pack(side='left')

        self.user_graph = None

    def run(self):
        self.root.mainloop()

    def build_graph_from_file(self):

        # "../graph_custom.csv"
        self.user_graph = graph_operations.GraphOperator.from_filename(self.e3.get())
        self.put_on_gui()

    def build_graph_randomly(self):

        self.user_graph = graph_operations.GraphOperator.from_random_generator(int(self.e2.get()), float(self.e1.get()))

        # Color it randomly
        self.color_it_randomly(int(self.e4.get()))

        self.put_on_gui()

    def run_algorithm(self):

        self.user_graph.dsatur_Algorithm()

        self.e4 = tk.Entry(self.root)
        self.e4.insert(23, f"colors used : {self.user_graph.get_max_color_after_algorithm()}")
        self.e4.pack(side='top')

        self.e5 = tk.Entry(self.root)
        self.e5.insert(23, f"time: {self.user_graph.get_time()}")
        self.e5.pack(side='top')

        self.put_on_gui()

    def color_it_randomly(self, to_color_nodes):

        for i in range(0, to_color_nodes+1):
            self.user_graph.assign_color_to_node(random.randrange(0, self.user_graph.node_count), i)

    def put_on_gui(self):

        f = plt.figure(figsize=(5, 4))
        plt.axis('off')
        plt.axis('off')

        pos = nx.circular_layout(self.user_graph.graph)

        max_color_intensity = self.user_graph.get_max_color_after_algorithm()
        if max_color_intensity <= 17:
            labeldict = []
            for i in range(0, self.user_graph.node_count):
                labeldict.append(graph_painter.ColorCodes.colors[self.user_graph.graph.nodes[i]["color"]])
            nx.draw_networkx(self.user_graph.graph, pos=pos, node_color=labeldict)
        else:
            labeldict = {}
            for i in range(0, self.user_graph.node_count):
                labeldict[i] = self.user_graph.graph.nodes[i]["color"]
            nx.draw_networkx(self.user_graph.graph, pos=pos, labels=labeldict)

        canvas = FigureCanvasTkAgg(f, master=self.root)
        canvas.get_tk_widget().pack(side='left', expand=1)  # ERROR Tk.


