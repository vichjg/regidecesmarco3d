import Matrices

class Vector(object):
    def __init__(self, y=0):
        self.n=None
        self.x=None
        if type(y) == int:
            self.n=y;
            self.x=[]
            for i in range(self.n):
                self.x.append(0)
        elif type(y) is list:
            self.x=y;
            self.n=len(self.x)
        else:
            print "error en vector"
    def __str__(self):
        texto = " "
        for i in range(self.n):
            texto = texto+"\t "+str(self.x[i])
        texto=texto+"\n"
        return texto
    
    @staticmethod
    def suma(a, b):
        resultado=Vector(a.n)
        for i in range(a.n):
            resultado.x[i]=a.x[i]+b.x[i]
        return resultado
    
    @staticmethod
    def resta(a,b):
        resultado=Vector(a.n)
        for i in range(a.n):
            resultado.x[i]=a.x[i]-b.x[i]
        return resultado
        
    
    @staticmethod
    def producto(a,b):
        if((type(a) == int or type(a) == float) and type(b) == Vector):
            resultado=Vector(b.n)
            for i in range(b.n):
                resultado.x[i]=a*b.x[i]
            return resultado
        elif type(a) == Vector and type(b) == Matrices.Matriz:
            n=a.n
            c=Vector(n)
            for j in range(n):
                for k in range(n):
                    c.x[j]+=a.x[k]*b.x[k][j]
            return c
        elif type(a) == Matrices.Matriz and type(b) == Vector:
            n=a.n
            c=Vector(n)
            for j in range(n):
                for k in range(n):
                    c.x[j]+=b.x[k]*a.x[k][j]
            return c
        else:
            return "error en producto - Vector"
        
    def modulo(self):
        if(self.n==1):
            return self.x[0]
        elif(self.n==2):
            return (self.x[0]**2+self.x[1]**2)**0.5
        elif(self.n==3):
            return (self.x[0]**2+self.x[1]**2+self.x[2]**2)**0.5
        else:
            print "error en modulo - vector"
            return
    
    @staticmethod
    def cruz(a,b):
        if(a.n==3 and b.n==3):
            c=Vector(3)
            c.x[0]=a.x[1]*b.x[2]-a.x[2]*b.x[1]
            c.x[1]=a.x[2]*b.x[0]-a.x[0]*b.x[2]
            c.x[2]=a.x[0]*b.x[1]-a.x[1]*b.x[0]
            return c
        else:
            print "error en producto cruz"
            return
    
    @staticmethod
    def cruzunitario(a,b):
        if(a.n==3 and b.n==3):
            return Vector.producto(1/Vector.cruz(a,b).modulo(),Vector.cruz(a,b))
        else:
            print "error en producto cruz unitario"
            return
        
    @staticmethod
    def productopunto(a,b):    
        if(a.n==2 and b.n==2):
            return a.x[0]*b.x[0]+a.x[1]*b.x[1]
        elif(a.n==3 and b.n==3):
            return a.x[0]*b.x[0]+a.x[1]*b.x[1]+a.x[2]*b.x[2]
        else:
            print "error en producto punto"
            
    @staticmethod
    def cosdirector(a,b):
        return Vector.productopunto(a,b)/(a.modulo()*b.modulo())   