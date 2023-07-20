from copy import deepcopy
import Vectores
import Graeffe

class Matriz(object):
    #Constructor principal, recibe un parametro que puede ser una lista o un entero
    def __init__(self, y=0):
        #si el parametro y=0 o no se especifica simplemente crea espacio de memoria para "n" y "x"
        self.n=None
        self.x=None
        if y != 0:
            #si el parametro "y" es un entero distinto de cero, guarda en n (que es el rango) ese valor
            #en x guarda una lista anidada en otra lista, de n valores cada una que son puros ceros
            if type(y) == int:
                self.n=y
                self.x=[]
                for i in range(self.n):
                    self.x.append([])
                    for j in range(self.n):
                        self.x[i].append(0)
            #si "y" es una lista, guarda en x esa lista con valores que pueden ser distintos de cero
            #es decir una matriz, y "n" sera longitud de esa lista o el rango de esa matriz
            elif type(y) is list:
                self.x=y
                self.n=len(self.x)
            else:
                print "error en matriz"
    
    def __str__(self):
        texto="\n"
        for i in range(self.n):
            for j in range(self.n):
                texto=texto+"\t "+str(self.x[i][j])
            texto=texto+"\n"
        texto=texto+"\n"
        return texto
    
    def clone(self):
        obj=Matriz()
        obj=deepcopy(self)
        return obj
    
    def traza(self):
        tr=0.0
        for i in range(self.n):
            tr+=self.x[i][i]
        return tr
        
    @staticmethod
    def suma(a, b):
        resultado=Matriz(a.n)
        for i in range(a.n):
            for j in range(a.n):
                resultado.x[i][j]=a.x[i][j]+b.x[i][j]
        return resultado
    
    @staticmethod
    def producto(a,b):
        if (type(a) == int or type(a) == float) and (type(b) == Matriz or type(b) == Vectores.Vector):
            resultado=Matriz(b.n)
            for i in range(b.n):
                for j in range(b.n):
                    resultado.x[i][j]=b.x[i][j]*a
            return resultado
        elif type(a) == Matriz and type(b) == Matriz:
            resultado=Matriz(a.n)
            for i in range(a.n):
                for j in range(a.n):
                    for k in range(a.n):
                        resultado.x[i][j]+=a.x[i][k]*b.x[k][j]
            return resultado;
        elif type(a) == Matriz and type(b) == Vectores.Vector:
            n=b.n  
            c=Vectores.Vector(n)
            for i in range(n):
                for k in range(n):
                    c.x[i]+=a.x[i][k]*b.x[k]
            return c
        else:
            return "error de producto - Matriz"
    
    def traspuesta(self):
        n=self.n
        resultado=Matriz(self.n)
        for i in range(n):
            for j in range(n):
                resultado.x[i][j]=self.x[j][i]
        return resultado
    
    def determinante(self):
        n=self.n
        a=self.clone()
        for k in range(n-1):
            for i in range(k+1,n):
                for j in range(k+1,n):
                    a.x[i][j]-=a.x[i][k]*a.x[k][j]/a.x[k][k]
        for i in range(1,n):
            for j in range(i):
                a.x[i][j]=0
        deter=1.0
        for i in range(n):
            deter*=a.x[i][i]
        return deter;
    
    def inversa(d):
        n=d.n
        a=d.clone()
        b=Matriz(n)
        c=Matriz(n)
        for i in range(n):
            b.x[i][i]=1.0
        for k in range(n-1):
            for i in range(k+1,n):
                for s in range(n):
                    b.x[i][s]-=a.x[i][k]*b.x[k][s]/a.x[k][k]
                for j in range(k+1,n):
                    a.x[i][j]-=a.x[i][k]*a.x[k][j]/a.x[k][k]
        for s in range(n):
            c.x[n-1][s]=b.x[n-1][s]/a.x[n-1][n-1]
            for i in range(n-2,-1,-1):
                c.x[i][s]=b.x[i][s]/a.x[i][i]
                for k in range(n-1,i,-1):
                    c.x[i][s]-=a.x[i][k]*c.x[k][s]/a.x[i][i]
        return c
    
    def polCaracteristico(self):
        n=self.n
        pot=Matriz(n)
        for i in range(n):
            pot.x[i][i]=1.0
        p=[]
        s=[]
        
        s.append(0.0)
        for i in range(1,n+1):
            pot=Matriz.producto(pot, self)
            s.append(pot.traza())
            
        p.append(1.0)
        p.append(-s[1])
        
        for i in range(2,n+1):
            p.append(-s[i]/i)
            for j in range(1,i):
                p[i]-=s[i-j]*p[j]/i
        return p
    
    def eigenvectores(self):
        pol=self.polCaracteristico()
        print pol
        g=Graeffe.Graeffe(pol)
        g.hallarRaicesNewton()
        print g.raices
        lambda_l=g.raices
        ind=[]
        matriz_M=[]
        for i in range(self.n-1):
            matriz_M.append([])
            for j in range(self.n-1):
                matriz_M[i].append(0)
        for i in range(self.n-1):
            ind.append(-self.x[i+1][0])
        eigen_vectores=Matriz(self.n)
        
        Y=Vectores.Vector(ind)
        M=Matriz(matriz_M)
        #print eigen_vectores
        print Y
        for i in range(len(lambda_l)):
            for j in range(1,self.n):
                for k in range(1,self.n):
                    M.x[j-1][k-1]=self.x[j][k]
                    if j==k:
                        M.x[j-1][k-1]*=(1-lambda_l[i])
            print M
            value=Matriz.producto(M.inversa(),Y)
            eigen_vectores.x[i][0]=1
            for p in range(1,self.n):
                eigen_vectores.x[i][p]=value.x[p-1]
            print eigen_vectores