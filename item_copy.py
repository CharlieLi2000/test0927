class Node:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.name: str = None
        self.x: float = None    # bottom-left
        self.y: float = None    # bottom-left
        self.w: int = None
        self.h: int = None
        self.edge_set: set[Edge] = set()

    def getCenter(self) -> tuple[float, float]:
        return (self.x + self.w / 2, self.y + self.h / 2)
    
    def setCenter(self, pos: tuple[float, float]) -> None:
        (x,y) = pos
        self.x = x - self.w / 2
        self.y = y - self.h / 2

    def pull(self) -> None:
        x_sum = 0.0
        y_sum = 0.0
        w_sum = 0.0
        for edge in self.edge_set:
            w = edge.pseudoWeight()
            if w > 0: 
                for node in edge.node_set:
                    x, y = node.getCenter()
                    x_sum += w * x
                    y_sum += w * y
                    w_sum += w
        if w_sum > 0:
            x = x_sum / w_sum
            y = y_sum / w_sum
            self.setCenter((x,y))

class Edge:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.name: str = None
        self.degree: int = None
        self.in_pin_list: list[tuple[Node, float, float]] = []
        self.out_pin_list: list[tuple[Node, float, float]] = []
        self.node_set: set[Node] = set()
    
    def pseudoWeight(self) -> float:
        d = len(self.node_set)
        return 1 / d if 2 <= d <= 10 else 0.0

class SuperNode:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.x: float = None
        self.y: float = None

class SuperEdge:
    def __init__(self, id: int) -> None:
        self.id: int = id