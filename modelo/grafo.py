
class Grafo:
    """_summary_ grafo almacenado en un diccionario    
    """
    def __init__(self,nodos,matriz_inciden):
        self.nodos = nodos
        self.matriz_inciden = matriz_inciden
        

    def imprimir(self):
        print("grafo creado")
