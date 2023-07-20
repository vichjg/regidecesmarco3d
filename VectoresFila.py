import Matrices
import Vectores
import VectoresColumna

class VectorFila(object):
    def __init__(self, y=0):
        self.n=None
        self.x=None
        if type(y) == int:
            self.n=y;
            self.x=[]
            for i in range(self.n):
                self.x.append(0)
                #Prueba print self.x[i],
        elif type(y) is list:
            self.x=y;
            self.n=len(self.x)
        else:
            print "error en vector fila"
    def __str__(self):
        texto = " "
        for i in range(self.n):
            texto = texto+"\t "+str(self.x[i])
        texto=texto+"\n"
        return texto
    
    @staticmethod
    def producto(a,b):
        if type(a) == Vectores.Vector and type(b) == Matrices.Matriz:
            n=a.n
            c=Vector(n)
            for j in range(n):
                for k in range(n):
                    c.x[j]+=a.x[k]*b.x[k][j]
            return c
        elif type(a) == VectorFila and type(b) == VectoresColumna.VectorColumna:
            n=a.n
            c=Matrices.Matriz(1)
            for i in range(n):
                c.x[0][0]+=a.x[i]*b.x[i]
            return c
        elif type(a) == VectoresColumna.VectorColumna and type(b) == VectorFila:
            n=a.n
            c=Matrices.Matriz(n)
            for i in range(n):
                for j in range(n):
                    c.x[i][j]=a.x[i]*b.x[j]
            return c
        else:
            return "error en producto - VectorFila"