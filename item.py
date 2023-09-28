class Node:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.name: str = None
        self.is_movable: bool = None
        self.w: int = None
        self.h: int = None
        self.area: int = None
        self.in_pin_list: list[tuple[Edge, float, float]] = []
        self.out_pin_list: list[tuple[Edge, float, float]] = []
        self.edge_set: set[Edge] = set()
        self.supernode_id: int = None
        self.num_pins_in = lambda : len(self.in_pin_list)
        self.num_pins_out = lambda : len(self.out_pin_list)
        self.num_pins = lambda : len(self.in_pin_list) + len(self.out_pin_list)
        self.edge_degree = lambda : len(self.edge_set)

class Edge:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.name: str = None
        self.degree: int = None
        self.in_pin_list: list[tuple[Node, float, float]] = []
        self.out_pin_list: list[tuple[Node, float, float]] = []
        self.node_set: set[Node] = set()
        self.supernode_id_set: set[int] = set()
    
    def pseudoWeight(self) -> float:
        d = len(self.node_set)
        return 1 / d if 2 <= d <= 30 else 0.0

class SuperNode:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.x: float = None
        self.y: float = None
        self.num_nodes: int = None
        self.area: int = None
        self.num_pins: int = None
        self.node_id_list: list[int] = []
        self.superedge_id_set: set[int] = set()
        self.edge_degree = lambda : len(self.superedge_id_set)

class SuperEdge:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.supernode_id_set: set[int] = set()