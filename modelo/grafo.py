

from gui.graficar_grafo import Graficar_grafo


class Grafo:
    """_summary_ grafo almacenado en un diccionario    
    """
    def __init__(self, nodes, edges, adjacencies):
        
        self.nodes = nodes
        self.edges = edges        
        self.adjacencies = adjacencies
        
    def get_nodes(self):
        return self.nodes
    def get_edges(self):
        return self.edges
    def get_adjacencies(self):
        return self.adjacencies
    