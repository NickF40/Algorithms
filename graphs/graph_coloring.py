from graphs.graph import GraphNode

colors = [
    "red", "green", "white",
    "black", "lime", "brown",
    "pink", "gray"
]


a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')
d = GraphNode('d')
e = GraphNode('e')
f = GraphNode('f')
g = GraphNode('g')


a.neighbours.add(b)
a.neighbours.add(f)

b.neighbours.add(a)
b.neighbours.add(c)
b.neighbours.add(g)

c.neighbours.add(b)
c.neighbours.add(d)
c.neighbours.add(g)

e.neighbours.add(d)

d.neighbours.add(e)
d.neighbours.add(c)
d.neighbours.add(f)

f.neighbours.add(d)
f.neighbours.add(g)
f.neighbours.add(a)

g.neighbours.add(b)
g.neighbours.add(f)
g.neighbours.add(c)


graph = [a, b, c, d, e, f, g]

d = 3


import pdb
pdb.set_trace()

for node in graph:
    if not node.color:
        for i in range(0, d):
            node.color = colors[i]
            print(node.label, node.color, list(node.neighbours))
            for neighbour in node.neighbours:
                j = i + 1
                print([step_neighbour.color for step_neighbour in neighbour.neighbours])
                if not neighbour.color and colors[j] not in [step_neighbour.color for step_neighbour in neighbour.neighbours]:
                    neighbour.color = colors[j]
                    print(neighbour.label, neighbour.color)
                    break
                else:
                    continue

print(graph)
