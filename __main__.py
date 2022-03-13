from modelo.grafo import Grafo
from gui.graficar_grafo import Graficar_grafo

def main():
    
    #g1 = Grafo(2,3)
    #g1.imprimir()
    diccion = {
        "A":["B"],
        "B":["C","E"],
        "C":["E"],
        "D":["A"],
        "E":["D"]
    }

    grap_grafo = Graficar_grafo(diccion)
    grap_grafo.draw_grafo(diccion)


if __name__ == '__main__':
    main()