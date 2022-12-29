import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk
import networkx as nx

import graph_operations


class GraphGraphicalInterface:

    def __init__(self):
        self.root = tk.Tk()

        self.b1 = tk.Button(self.root, text="Build a random graph", command=self.build_graph)
        self.b1.pack(side='right')

        self.e1 = tk.Entry(self.root)
        self.e1.insert(0, 'Intensity')
        self.e1.pack(side='right')

        self.e2 = tk.Entry(self.root)
        self.e2.insert(0, 'NodeCount')
        self.e2.pack(side='right')

        self.b2 = tk.Button(self.root, text="Build from filename", command=self.build_graph_from_file)
        self.b2.pack(side='left')

        self.e3 = tk.Entry(self.root)
        self.e3.insert(0, 'filename')
        self.e3.pack(side='left')

    def run(self):
        self.root.mainloop()

    def build_graph_from_file(self):
        f = plt.figure(figsize=(5, 4))
        plt.axis('off')
        plt.axis('off')

        a = graph_operations.GraphOperator.from_filename("../graph_custom.csv")

        # Input color.
        a.dsatur_Algorithm()

        pos = nx.circular_layout(a.graph)

        labeldict = {}
        for i in range(0, a.node_count):
            labeldict[i] = a.graph.nodes[i]["color"]

        nx.draw_networkx(a.graph, pos=pos, labels=labeldict)
        canvas = FigureCanvasTkAgg(f, master=self.root)
        canvas.get_tk_widget().pack(side='bottom', fill='both', expand=1)  # ERROR Tk.

    def build_graph(self):
        f = plt.figure(figsize=(5, 4))
        plt.axis('off')
        plt.axis('off')

        a = graph_operations.GraphOperator.from_random_generator(int(self.e2.get()), float(self.e1.get()))

        # Input color.
        a.assign_color_to_node(1, 1)
        a.dsatur_Algorithm()

        pos = nx.circular_layout(a.graph)

        labeldict = {}
        for i in range(0, a.node_count):
            labeldict[i] = a.graph.nodes[i]["color"]

        nx.draw_networkx(a.graph, pos=pos, labels=labeldict)
        canvas = FigureCanvasTkAgg(f, master=self.root)
        canvas.get_tk_widget().pack(side='bottom', fill='both', expand=1)  # ERROR Tk.
