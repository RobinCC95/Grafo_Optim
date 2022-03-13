
from PIL import ImageTk, Image
from graphviz import Digraph


class Graficar_grafo:
    """_summary_ clase encargada de graficar el grafo 
    """
    def __init__(self, matriz_inciden):
        self.dat_grafo = Digraph('G',filename='grafo',format='png')
        self.matriz_inciden = matriz_inciden




    def crear_nodos(self,matriz_inciden):
        for k in matriz_inciden.keys():
            self.dat_grafo.node(str(k), label=str(k), color='black',fontcolor='black',fillcolor='white',style='filled',fontname = "consolas",fontsize = "16")
			
    def crear_adyacencias(self, matriz_inciden):
        for key, item in matriz_inciden.items():
            for dat in item:
                self.dat_grafo.edge(str(key), str(dat), label="" ,color='#01c952',penwidth='3')




    def draw_grafo(self, matriz_inciden):
        """adiciona parametros al grafico y el nodo

        Args:
            matriz_inciden (dicc): diccionario de incidencia del grafo
        """
        self.dat_grafo.attr(rankdir ='LR', size = '80')
        self.dat_grafo.attr('node', shape= 'box3d')
        self.dat_grafo.attr(bgcolor='#abdbe3',fontcolor='white')
        self.crear_nodos(matriz_inciden)
        self.crear_adyacencias(matriz_inciden)

        #graficar
        self.dat_grafo.view()






