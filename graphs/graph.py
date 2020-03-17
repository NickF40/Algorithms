class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbours = set()
        self.color = None

    def __str__(self):
        return ":".join([self.label, self.color])

    def __repr__(self):
        return ":".join([self.label, self.color])
