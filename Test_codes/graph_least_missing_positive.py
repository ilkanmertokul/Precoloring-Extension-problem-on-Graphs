import graph_operations as go

g = go.GraphOperator(100, 0.2)

arr = g.graph.neighbors(10)
print(arr)
i=1
for a in arr:
    g.assign_color_to_node(a, i)
    print(g.graph.nodes[a]["color"])
    i = i+1

print("-")
print(g.get_assignable_color_intensity(10))
