from __version__ import *

class Module:
    def __init__(self):
        self.version = "v0.1.0+draft" 
        self.graph = dict()
        self.operator = dict()
        self.type = dict()
        self.meta = dict()

class Graph(Module):
    def __init__(self) -> None:
        super().__init__()

class Operator:
    def __init__(self) -> None:
        pass