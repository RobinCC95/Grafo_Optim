from modelo.grafo import Grafo
from gui.graficar_grafo import Graficar_grafo

def main():
    
    diccion = {
        "A":["B","D"],
        "B":["C","E"],
        "C":["E"],
        "D":["A"],
        "E":["D"]
    }
    g = Grafo(diccion)
    g.draw_g()



if __name__ == '__main__':
    main()