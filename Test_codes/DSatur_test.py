import graph_operations

a = graph_operations.GraphOperator.from_random_generator(100, 0.2)

a.assign_color_to_node(1, 2)
a.assign_color_to_node(2, 3)

a.dsatur_Algorithm()
