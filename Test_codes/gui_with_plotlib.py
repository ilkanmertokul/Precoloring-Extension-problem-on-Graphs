import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk
import networkx as nx

import graph_operations

nodecount = 15
intensity = 0.3


def build_graph():
    f = plt.figure(figsize=(5, 4))
    plt.axis('off')
    plt.axis('off')

    G = graph_operations.GraphOperator(int(e2.get()), float(e1.get()))
    pos = nx.circular_layout(G.graph)

    labeldict = {}
    for i in range(0, len(G.graph.nodes)):
        labeldict[i] = 0

    nx.draw_networkx(G.graph, pos=pos, labels=labeldict)
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.get_tk_widget().pack(side='bottom', fill='both', expand=1)  # ERROR Tk.


root = tk.Tk()

b1 = tk.Button(root, text="Build a random graph", command=build_graph)
b1.pack(side='right')

e1 = tk.Entry(root)
e1.insert(0, 'Intensity')
e1.pack(side='right')

e2 = tk.Entry(root)
e2.insert(0, 'NodeCount')
e2.pack(side='right')

root.mainloop()
