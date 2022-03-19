

from gui.graficar_grafo import Graficar_grafo


class Grafo:
    """_summary_ grafo almacenado en un diccionario    
    """
    def __init__(self, matriz_ady, peso_nodo=None):
        """contructor del grafo relacionado por una matriz de adyacencia y unos pesos
        en los vertices        

        Args:
            matriz_inciden (Dicc): matriz de adyacencia relacionando nodo->[nodo_i,...,nodo_n]
            peso_nodo (Dicc): peso de cada nodo->peso
        """
        self.matriz_ady = matriz_ady
        self.peso_nodo = peso_nodo
        

    def imprimir(self):
        print("grafo creado")

    def get_matriz_ady(self):
        if len(self.matriz_ady)>0:
            return self.matriz_ady
        return None

    def get_peso_nodo(self):
        if len(self.get_peso_nodo)>0:
            return self.get_peso_nodo
        return None    

    def draw_g(self):
        dicc_ady = self.get_matriz_ady()
        gg1 = Graficar_grafo(dicc_ady)
        gg1.draw_grafo()
    
    def string_grafo(self):
        return "grafo enviado"