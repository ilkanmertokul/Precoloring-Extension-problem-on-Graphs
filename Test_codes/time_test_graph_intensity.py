import graph_operations

vertex_amount = 1000
intensity_amount = 0.1
color_amount = 100
timetable = []

for i in range(0, 9):
    timetable.append(0)

for i in range(0, 9):
    for j in range(0, 50):
        a = graph_operations.GraphOperator.from_random_generator(vertex_amount, intensity_amount + i*intensity_amount)
        a.assign_color_to_node(1,1)
        a.dsatur_Algorithm()
        timetable[i] += a.time

for i in range(0, 9):
    print(f"Average -> ({intensity_amount + i*intensity_amount},{timetable[i] / 50})")

