
import graph_operations

increment_amount = 250
intensity_amount = 0.5
timetable = []

for i in range(0,10):
    timetable.append(0)

for i in range(0,10):
    for j in range(0,50):
        a = graph_operations.GraphOperator.from_random_generator(increment_amount + i*increment_amount, intensity_amount)
        a.assign_color_to_node(1,1)
        a.dsatur_Algorithm()
        timetable[i] += a.time

for i in range(0,10):
    print(f"Average {increment_amount + i*increment_amount} -> ({timetable[i]/50})")



