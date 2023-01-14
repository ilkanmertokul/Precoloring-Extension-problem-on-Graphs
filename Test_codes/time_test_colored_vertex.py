import graph_operations

vertex_amount = 1000
intensity_amount = 0.5
color_amount = 100
timetable = []

for i in range(0, 9):
    timetable.append(0)

for i in range(0, 9):
    for j in range(0, 50):
        a = graph_operations.GraphOperator.from_random_generator(vertex_amount, intensity_amount)
        for k in range(0, color_amount + i * color_amount):
            a.assign_color_to_node(k, k)
        a.dsatur_Algorithm()
        timetable[i] += a.time

for i in range(0, 9):
    print(f"Average -> ({color_amount + i * color_amount},{timetable[i] / 50})")

