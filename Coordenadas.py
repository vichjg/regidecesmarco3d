import VectoresColumna
import Vectores

class Coordenada(object):
    #reacciones=VectoresColumna.VectorColumna(2)
    
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
        self.deflexion=Vectores.Vector(6)
        self.reacciones=Vectores.Vector(6)