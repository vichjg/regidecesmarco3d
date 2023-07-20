import Matrices
import Vectores

class Barra(object):
    fuerzai=None
    fuerzaj=None
    modificador=False
    #fuerza_ij=None
    #fuerza_ji=None
    
    def __init__(self,A,E,G,Ix,Iy,J,coord,inicial,final):
        self.A=A
        self.E=E
        self.G=G
        self.Ix=Ix
        self.Iy=Iy
        self.J=J
        self.inicial=inicial
        self.final=final
        
        self.coord1=coord[inicial]
        self.coord2=coord[final]
        
        self.vinicial=Vectores.Vector(3)
        self.vinicial.x[0]=self.coord1.x
        self.vinicial.x[1]=self.coord1.y
        self.vinicial.x[2]=self.coord1.z
        self.vfinal=Vectores.Vector(3)
        self.vfinal.x[0]=self.coord2.x
        self.vfinal.x[1]=self.coord2.y
        self.vfinal.x[2]=self.coord2.z
        self.L=Vectores.Vector.resta(self.vfinal,self.vinicial).modulo()
        self.xuni=Vectores.Vector([1,0,0])
        self.yuni=Vectores.Vector([0,1,0])
        self.zuni=Vectores.Vector([0,0,1])
        
        self.zpuni=Vectores.Vector.producto(1/Vectores.Vector.modulo(Vectores.Vector.resta(self.vfinal,self.vinicial)),Vectores.Vector.resta(self.vfinal,self.vinicial))
        print "vectores"
        print self.zpuni
        if(Vectores.Vector.cosdirector(self.yuni,self.zpuni)==1 or Vectores.Vector.cosdirector(self.yuni,self.zpuni)==-1):
            self.ypuni=Vectores.Vector([1,0,0])
            print self.ypuni
        else:
            self.xpuni=Vectores.Vector.cruzunitario(self.yuni,self.zpuni)
        if(Vectores.Vector.cosdirector(self.yuni,self.zpuni)==1 or Vectores.Vector.cosdirector(self.yuni,self.zpuni)==-1):
            #self.xpuni=Vectores.Vector.cruzunitario(self.ypuni,self.zpuni)
            self.xpuni=Vectores.Vector([0,0,1])
            print self.xpuni
        else:
            self.ypuni=Vectores.Vector.cruz(self.zpuni,self.xpuni)
        
        
        self.cosa1=Vectores.Vector.cosdirector(self.xuni,self.xpuni)
        self.cosa2=Vectores.Vector.cosdirector(self.xuni,self.ypuni)
        self.cosa3=Vectores.Vector.cosdirector(self.xuni,self.zpuni)
        
        self.cosb1=Vectores.Vector.cosdirector(self.yuni,self.xpuni)
        self.cosb2=Vectores.Vector.cosdirector(self.yuni,self.ypuni)
        self.cosb3=Vectores.Vector.cosdirector(self.yuni,self.zpuni)
        
        self.cosy1=Vectores.Vector.cosdirector(self.zuni,self.xpuni)
        self.cosy2=Vectores.Vector.cosdirector(self.zuni,self.ypuni)
        self.cosy3=Vectores.Vector.cosdirector(self.zuni,self.zpuni)
        
        self.tau=Matrices.Matriz([[self.cosa1,self.cosb1,self.cosy1],[self.cosa2,self.cosb2,self.cosy2],[self.cosa3,self.cosb3,self.cosy3]])
        self.lmbda=Matrices.Matriz([[self.cosy3,self.cosb3,self.cosa3,0,0,0,0,0,0,0,0,0],[self.cosy2,self.cosb2,self.cosa2,0,0,0,0,0,0,0,0,0],[self.cosy1,self.cosb1,self.cosa1,0,0,0,0,0,0,0,0,0],[0,0,0,self.cosy3,self.cosb3,self.cosa3,0,0,0,0,0,0],[0,0,0,self.cosy2,self.cosb2,self.cosa2,0,0,0,0,0,0],[0,0,0,self.cosy1,self.cosb1,self.cosa1,0,0,0,0,0,0]])
        self.lmbdat=self.lmbda.traspuesta()
        self.R=Matrices.Matriz([[self.cosy3,self.cosb3,self.cosa3,0,0,0,0,0,0,0,0,0],[self.cosy2,self.cosb2,self.cosa2,0,0,0,0,0,0,0,0,0],[self.cosy1,self.cosb1,self.cosa1,0,0,0,0,0,0,0,0,0],[0,0,0,self.cosy3,self.cosb3,self.cosa3,0,0,0,0,0,0],[0,0,0,self.cosy2,self.cosb2,self.cosa2,0,0,0,0,0,0],[0,0,0,self.cosy1,self.cosb1,self.cosa1,0,0,0,0,0,0],[0,0,0,0,0,0,self.cosy3,self.cosb3,self.cosa3,0,0,0],[0,0,0,0,0,0,self.cosy2,self.cosb2,self.cosa2,0,0,0],[0,0,0,0,0,0,self.cosy1,self.cosb1,self.cosa1,0,0,0],[0,0,0,0,0,0,0,0,0,self.cosy3,self.cosb3,self.cosa3],[0,0,0,0,0,0,0,0,0,self.cosy2,self.cosb2,self.cosa2],[0,0,0,0,0,0,0,0,0,self.cosy1,self.cosb1,self.cosa1]])
        self.Rt=self.R.traspuesta()
        
        raz=self.E*self.A/self.L
        rj=self.G*self.J/self.L
        raax=12*self.E*self.Ix/self.L**3
        rabx=rbax=6*self.E*self.Ix/self.L**2
        r11x=r22x=4*self.E*self.Ix/self.L
        r12x=r21x=2*self.E*self.Ix/self.L
        raay=12*self.E*self.Iy/self.L**3
        raby=rbay=6*self.E*self.Iy/self.L**2
        r11y=r22y=4*self.E*self.Iy/self.L
        r12y=r21y=2*self.E*self.Iy/self.L
        
        
        self.kii=Matrices.Matriz([[raz,0,0,0,0,0],[0,raax,0,0,0,rabx],[0,0,raay,0,-raby,0],[0,0,0,rj,0,0],[0,0,-raby,0,r11y,0],[0,rabx,0,0,0,r11x]])
        self.kij=Matrices.Matriz([[-raz,0,0,0,0,0],[0,-raax,0,0,0,rbax],[0,0,-raay,0,-rbay,0],[0,0,0,-rj,0,0],[0,0,raby,0,r12y,0],[0,-rabx,0,0,0,r12x]])
        self.kji=self.kij.traspuesta()
        self.kjj=Matrices.Matriz([[raz,0,0,0,0,0],[0,raax,0,0,0,-rbax],[0,0,raay,0,rbay,0],[0,0,0,rj,0,0],[0,0,rbay,0,r22y,0],[0,-rbax,0,0,0,r22x]])
        
        self.Kii=Matrices.Matriz.producto(self.lmbdat,Matrices.Matriz.producto(self.kii,self.lmbda))
        self.Kij=Matrices.Matriz.producto(self.lmbdat,Matrices.Matriz.producto(self.kij,self.lmbda))
        self.Kji=Matrices.Matriz.producto(self.lmbdat,Matrices.Matriz.producto(self.kji,self.lmbda))
        self.Kjj=Matrices.Matriz.producto(self.lmbdat,Matrices.Matriz.producto(self.kjj,self.lmbda))
        
