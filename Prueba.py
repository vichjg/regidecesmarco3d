import math
import Vectores
import Coordenadas
import Barras
import Matrices
import Restricciones
import Fuerzas

if __name__ == "__main__":
    c1=Coordenadas.Coordenada(0,0,0)
    c2=Coordenadas.Coordenada(300,300,300)
    coordenadas=[c1,c2]
    
    b1=Barras.Barra(59.69,2000000,769230.8,2700,2700,5400,coordenadas,1-1,2-1)
    #print b1.zpuni
    #print b1.zpuni.modulo()
    #print b1.xpuni.modulo()
    #print b1.ypuni.modulo()
    print "cosa1",b1.cosa1
    print "cosa2",b1.cosa2
    print "cosa3",b1.cosa3
    print "cosb1",b1.cosb1
    print "cosb2",b1.cosb2
    print "cosb3",b1.cosb3
    print "cosy1",b1.cosy1
    print "cosy2",b1.cosy2
    print "cosy3",b1.cosy3
    #print b1.xpuni
    #print b1.yuni
    
    print b1.tau
    print b1.tau.traspuesta()
    
    print b1.lmbda
    print "Matriz de rotacion"
    print b1.R
    print "R.inversa"
    #print b1.R.inversa()
    print b1.R.traspuesta()
    
    print b1.kii
    
    '''
    b1=Barras.Barra(900,238000,67500,coordenadas,1-1,2-1)
    b2=Barras.Barra(900,238000,67500,coordenadas,1-1,3-1)
    b3=Barras.Barra(900,238000,67500,coordenadas,2-1,4-1)'''
    
    barras=[b1]

    #Matriz de rigidez global:
    K=Matrices.Matriz(6*len(coordenadas))
    
    for i in range(len(barras)): #para i desde 0 hasta el numero de barras
        for j in range(6):
            for k in range(6):
                K.x[6*barras[i].inicial+j][6*barras[i].inicial+k]+=barras[i].Kii.x[j][k]
                K.x[6*barras[i].inicial+j][6*barras[i].final+k]+=barras[i].Kij.x[j][k]
                K.x[6*barras[i].final+j][6*barras[i].inicial+k]+=barras[i].Kji.x[j][k]
                K.x[6*barras[i].final+j][6*barras[i].final+k]+=barras[i].Kjj.x[j][k]
    print K
    
    r1=Restricciones.Restriccion(1-1,True,True,True,True,True,True)
    
    restricciones=[r1]
    
    GDLrestringidos=[]
    for i in range(len(restricciones)):
        if(restricciones[i].x==True):
            GDLrestringidos.append(6*restricciones[i].coord)
        if(restricciones[i].y==True):
            GDLrestringidos.append(6*restricciones[i].coord+1)
        if(restricciones[i].z==True):
            GDLrestringidos.append(6*restricciones[i].coord+2)
        if(restricciones[i].mx==True):
            GDLrestringidos.append(6*restricciones[i].coord+3)
        if(restricciones[i].my==True):
            GDLrestringidos.append(6*restricciones[i].coord+4)
        if(restricciones[i].mz==True):
            GDLrestringidos.append(6*restricciones[i].coord+5)
    
    print "GDL Restringidos",GDLrestringidos
    
    matrizDeRigidez=Matrices.Matriz(6*len(coordenadas)-len(GDLrestringidos))
    
    GDLnoRestringidos=[]
    for i in range(K.n):
        if(i in GDLrestringidos):
            continue
        GDLnoRestringidos.append(i)
    
    print "GDL No restringidos",GDLnoRestringidos
    
    m=0
    for i in GDLnoRestringidos:
        l=0
        for j in GDLnoRestringidos:
            matrizDeRigidez.x[l][m]+=K.x[i][j]
            l+=1
        m+=1
        
    print "Matriz de rigidez de la estructura"
    print matrizDeRigidez
    print "Matriz de flexibilidad de la estructura"
    print matrizDeRigidez.inversa()
    
    
    p1=Fuerzas.Fuerza(2-1,100,200,300,400,500,600)
    
    P=[p1]

    vectorDeFuerzas=Vectores.Vector(6*len(coordenadas)-len(GDLrestringidos))
    
    n=0
    for i in range(6*len(P)):
        if(i in GDLnoRestringidos):
           continue
        a=int(i/6)
        if(i%6==0):
            vectorDeFuerzas.x[n]=P[a].x
        if(i%6==1):
            vectorDeFuerzas.x[n]=P[a].y
        if(i%6==2):
            vectorDeFuerzas.x[n]=P[a].z
        if(i%6==3):
            vectorDeFuerzas.x[n]=P[a].Mx
        if(i%6==4):
            vectorDeFuerzas.x[n]=P[a].My
        if(i%6==5):
            vectorDeFuerzas.x[n]=P[a].Mz
        n+=1
    
            
    print vectorDeFuerzas
    
    Desplazamientos=Vectores.Vector.producto(matrizDeRigidez.inversa(),vectorDeFuerzas)
    
    print Desplazamientos
    
    Delta=Vectores.Vector(6*len(coordenadas))
    
    l=0
    for i in range(6*len(coordenadas)):
        if(i in GDLnoRestringidos):
            a=int(i/6)
            if(i%6==0):
                coordenadas[a].deflexion.x[0]=Desplazamientos.x[l]
            elif(i%6==1):
                coordenadas[a].deflexion.x[1]=Desplazamientos.x[l]
            elif(i%6==2):
                coordenadas[a].deflexion.x[2]=Desplazamientos.x[l]
            elif(i%6==3):
                coordenadas[a].deflexion.x[3]=Desplazamientos.x[l]
            elif(i%6==4):
                coordenadas[a].deflexion.x[4]=Desplazamientos.x[l]
            else:
                coordenadas[a].deflexion.x[5]=Desplazamientos.x[l]
            l+=1
        if(i in GDLrestringidos):
            b=int(i/6)
            if(i%6==0):
                coordenadas[b].deflexion.x[0]=0
            elif(i%6==1):
                coordenadas[b].deflexion.x[1]=0
            elif(i%6==2):
                coordenadas[b].deflexion.x[2]=0
            elif(i%6==3):
                coordenadas[b].deflexion.x[3]=0
            elif(i%6==4):
                coordenadas[b].deflexion.x[4]=0
            else:
                coordenadas[b].deflexion.x[5]=0
        c=int(i/6)
        if(i%6==0):
            Delta.x[i]=coordenadas[c].deflexion.x[0]
        if(i%6==1):
            Delta.x[i]=coordenadas[c].deflexion.x[1]
        if(i%6==2):
            Delta.x[i]=coordenadas[c].deflexion.x[2]
        if(i%6==3):
            Delta.x[i]=coordenadas[c].deflexion.x[3]
        if(i%6==4):
            Delta.x[i]=coordenadas[c].deflexion.x[4]
        if(i%6==5):
            Delta.x[i]=coordenadas[c].deflexion.x[5]
    
    print "Deflexiones"
    print Delta
    
    for i in range(len(barras)):
        barras[i].fuerzai=Vectores.Vector.suma(Matrices.Matriz.producto(Matrices.Matriz.producto(barras[i].kii,barras[i].lmbda),coordenadas[barras[i].inicial].deflexion),Matrices.Matriz.producto(Matrices.Matriz.producto(barras[i].kij,barras[i].lmbda),coordenadas[barras[i].final].deflexion))
        barras[i].fuerzaj=Vectores.Vector.suma(Matrices.Matriz.producto(Matrices.Matriz.producto(barras[i].kji,barras[i].lmbda),coordenadas[barras[i].inicial].deflexion),Matrices.Matriz.producto(Matrices.Matriz.producto(barras[i].kjj,barras[i].lmbda),coordenadas[barras[i].final].deflexion))
        print barras[i].fuerzai
        print barras[i].fuerzaj
        
    for i in GDLrestringidos:
        a=int(i/6)
        for j in range(len(barras)):
            if(barras[j].modificador==True):
                continue
            if(barras[j].inicial==a):
                coordenadas[a].reacciones=Vectores.Vector.producto(barras[j].lmbda,barras[j].fuerzai)
                barras[j].modificador=True
            if(barras[j].final==a):
                coordenadas[a].reacciones=Vectores.Vector.producto(barras[j].lmbda,barras[j].fuerzaj)
                barras[j].modificador=True   
        
    for i in range(len(coordenadas)):
        if(math.fabs(coordenadas[i].reacciones.x[0])<0.000001):
            coordenadas[i].reacciones.x[0]=0
        if(math.fabs(coordenadas[i].reacciones.x[1])<0.000001):
            coordenadas[i].reacciones.x[1]=0
        if(math.fabs(coordenadas[i].reacciones.x[2])<0.000001):
            coordenadas[i].reacciones.x[2]=0
        if(math.fabs(coordenadas[i].reacciones.x[3])<0.000001):
            coordenadas[i].reacciones.x[3]=0
        if(math.fabs(coordenadas[i].reacciones.x[4])<0.000001):
            coordenadas[i].reacciones.x[4]=0
        if(math.fabs(coordenadas[i].reacciones.x[5])<0.000001):
            coordenadas[i].reacciones.x[5]=0
                
    print "Reacciones:"
    for i in range(len(coordenadas)):
        print coordenadas[i].reacciones