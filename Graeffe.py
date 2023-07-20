import math

class Graeffe(object):
     
    def __init__(self,x=[1]):
        self.n=len(x)
        self.x=[]
        self.raices=[]
        self.CERO=0.001
        self.m=7 #exponente de 2^m, numero de veces que se repite el proceso, 
        #el exponente del polinomio con m=7 sera entonces 2^7=128, [P(x)]^128
        for i in range(self.m+1):
            self.x.append([])
            for j in range(self.n):
                self.x[i].append(x[j])
        self.tabla()
    
    def tabla(self):
        signo=0
        
        #Dividimos los coeficieentes principales entre a0
        for i in range(self.n-1,-1,-1):
            self.x[0][i]/=self.x[0][0]
        #Coeficientes cuadrados
        for l in range(self.m):
            for i in range(self.n):
                if i%2==0:
                    signo=+1.0
                else:
                    signo=-1.0
                self.x[l+1][i]=signo*self.x[l][i]**2
        #Dobles productos
            for i in range(self.n):
                if i == 0:
                    continue
                if i==len(self.x)-1:
                    break
                s=i
                k=i
                for j in range(i):
                    if (s-1)%2==0:
                        signo=1.0
                    else:
                        signo=-1.0
                    if (k+1)>=self.n:
                        break
                    if (s-1)<0:
                        break
                    #print i,signo,s-1,k+1
                    self.x[l+1][i]+=2*signo*self.x[l][s-1]*self.x[l][k+1]
                    s-=1
                    k+=1
            if len(self.x)%2==0:
                for i in range(self.n):
                    self.x[k+1][i]=-self.x[k+1][i]
        ''''''#1
        #for i in range(self.n):
            #print self.x[self.m][i]
        ''''''#1
        
    def valorPolinomio(self,x):
        pot_x=[]
        y=0.0
        for i in range(self.n-1):
            pot_x.append(1)
        j=0
        for i in range(self.n-2,-1,-1):
            pot_x[j]=x**(i+1)
            j+=1
        ''''''
        #for i in range(self.n-1):
            #print pot_x[i]
        ''''''
        for i in range(self.n-1):
            y+=self.x[0][i]*pot_x[i]
        y+=self.x[0][self.n-1]
        return y
        
    def calculaRaices(self):
        tentativa_raiz=[]
        for i in range(1,self.n):
            logaritmo=(math.log(math.fabs(self.x[self.m][i]))-math.log(math.fabs(self.x[self.m][i-1])))/(2.0**self.m)
            tentativa_raiz.append(math.exp(logaritmo))
        return tentativa_raiz
    
    def hallarRaicesGraeffe(self):
        tentativa_raiz=self.calculaRaices()
        for i in range(self.n-1):
            self.raices.append(0)
            if math.fabs(self.valorPolinomio(tentativa_raiz[i]))<self.CERO:
                self.raices[i]=tentativa_raiz[i]
            else:
                self.raices[i]=-tentativa_raiz[i]
    
    def mostrarRaices(self):
        self.hallarRaicesNewton()
        for i in range(len(self.raices)):
            if i==len(self.raices)-1:
                print self.raices[i]
                break
            print self.raices[i]," , ",
     
    def valorDerivada(self,x):
        y=0.0
        pot_x=[]
        for i in range(self.n-1):
            pot_x.append(1)
        j=0
        for i in range(self.n-2,-1,-1):
            pot_x[j]=x**(i)
            j+=1
        n=self.n-1
        for i in range(self.n-1):
            y+=self.x[0][i]*(n)*pot_x[i]
            n-=1
        return y
    
    def hallarRaicesNewton(self):
        self.hallarRaicesGraeffe()
        for i in range(len(self.raices)):
            for j in range(10000):
                if (self.valorPolinomio(self.raices[i])<0.00000000000000001)or(self.valorDerivada(self.raices[i])==0):
                    break
                #Algoritmo de Newton-Rapson
                self.raices[i]=self.raices[i]-self.valorPolinomio(self.raices[i])/self.valorDerivada(self.raices[i])
        
        

if __name__ == "__main__":
    g=Graeffe([1,-6,1,-6])
    g.mostrarRaices()