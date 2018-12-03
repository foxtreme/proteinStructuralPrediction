import math
import numpy as numeric
#import numpy.oldnumeric.mlab as mlab
from Bio.PDB import *

"""
para cada proteina en SCOPclassifications se compara el perfil normalizado
normalized/normalized-profile-(%s).txt con TODOS los perfiles normalizados
que hay en el conjunto de datos, luego se asigna su clasificacion scop usando
1-cos

al final se muestran los aciertos por class, fold, superfamily y family
"""

M=100 

todoslosdominios=list()
scop=dict()

f = open('sources/superfamily_level/lff5Random.txt','r')
lines = f.readlines()
f.close()

for x in lines:  
    y=x.split()[0]
    directory=y[3:5]
    name=y[1:len(y)]
    clase=x.split()[1]
    
    if name=='g1k3b.1': name='d1k3b.1'
    if name=='g1f2t.1': name='d1f2t.1'
    if name=='g1f8v.1': name='d1f8v.1'
    if name=='g2gac.1': name='d2gac.1'
    if name=='g1gk9.1': name='d1gk9.1'
    if name=='g1fm2.1': name='d1fm2.1'
    if name=='g1apy.1': name='d1apy.1'
    if name=='g1gg6.1': name='d1gg6.1'
    if name=='g1gj7.1': name='d1gj7.1'
    if name=='g1dy9.1': name='d1dy9.1'
    if name=='g1h8d.1': name='d1h8d.1'
    if name=='g1fiw.1': name='d1fiw.1'
    if name=='g1c5y.1': name='d1c5y.1'
    if name=='g1c5l.1': name='d1c5l.1'
    if name=='g2ltn.1': name='d2ltn.1'
    if name=='g1avo.1': name='d1avo.1'
    if name=='g1pnb.1': name='d1pnb.1'
    if name=='g1qrj.1': name='d1qrj.1'
    if name=='g1cxp.1': name='d1cxp.1'
    if name=='g1htr.1': name='d1htr.1'
    if name=='g1aw8.1': name='d1aw8.1'
    if name=='g1jot.2': name='d1jot.2'
    if name=='g1dgw.1': name='d1dgw.1'
    if name=='g1ibc.1': name='d1ibc.1'
    if name=='g1qtn.1': name='d1qtn.1'
    if name=='g1wht.1': name='d1wht.1'
    if name=='g1kve.1': name='d1kve.1'
    if name=='g1e3a.1': name='d1e3a.1'
    if name=='g1pya.1': name='d1pya.1'
    if name=='g1jen.3': name='d1jen.3'
    if name=='g1lts.1': name='d1lts.1'
    if name=='g1hle.1': name='d1hle.1'
    if name=='g1as4.1': name='d1as4.1'
    if name=='g1f0c.1': name='d1f0c.1'
    if name=='g1qd6.1': name='d1qd6.1'
    if name=='g1ben.1': name='d1ben.1'
    if name=='g6rlx.1': name='d6rlx.1'
    if name=='g1bom.1': name='d1bom.1'
    if name=='g2bi6.2': name='d2bi6.2'

    if name=='g1ku8.1': name='d1ku8.1'
    if name=='g1h6w.1': name='d1h6w.1'
    if name=='g1jjo.1': name='d1jjo.1'
    if name=='g1jmu.1': name='d1jmu.1'
    if name=='g1g7a.1': name='d1g7a.1'

    scop[name]=clase
    todoslosdominios.append(name) 

losConteos=dict()


for name in todoslosdominios:
    f = open('normalized/normalized-profile-(%s).txt'%(name),'r')    
    lines = f.readlines()
    f.close()

    count = list()

    for l in lines:
        d=l.split()

        for x in d:
            valor=float(x)
            count.append(valor)

    losConteos[name]=count


predicciones=list()
for i in range(len(todoslosdominios)):
    print i
    nombre1=todoslosdominios[i]
    distancias=list()
    
    for j in range(len(todoslosdominios)):

        if i!=j:
            name1=todoslosdominios[i]
            name2=todoslosdominios[j]
            valores1=losConteos[name1]
            valores2=losConteos[name2]

            myarray1 = numeric.asarray(valores1)
            myarray2 = numeric.asarray(valores2)
            ax1=sum(myarray1*myarray1)
            ax2=sum(myarray2*myarray2)        
            cos=sum(myarray1*myarray2)/math.sqrt(ax1*ax2)
            distancia=1-cos
            distancias.append(distancia)
        if i==j:
            distancias.append(2) # para que no escoja el mismo

   
    v=numeric.asarray(distancias)
    menor=v.argmin() 
    dominioSimilar=todoslosdominios[menor]
    clase1=scop[nombre1]
    clasePredicha=scop[dominioSimilar]
   
    tupla=list()
    tupla.append(clase1)
    tupla.append(clasePredicha)
    predicciones.append(tupla)

aF=0
aS=0
aL=0
aC=0
for x in predicciones:
    scop1=x[0]#clase real
    scop2=x[1]#clase predicha
    s1=scop1.split(".")
    s2=scop2.split(".")
    super1=s1[0] + "." + s1[1] + "." + s1[2]
    super2=s2[0] + "." + s2[1] + "." + s2[2]    
    fold1=s1[0] + "." + s1[1]
    fold2=s2[0] + "." + s2[1]
    class1=s1[0] 
    class2=s2[0] 

    if scop1==scop2:
        aF=aF+1
    if super1==super2:
        aS=aS+1
    if fold1==fold2:
        aL=aL+1
    if class1==class2:
        aC=aC+1
print "Family , Superfamily, Fold , Class"
print aF,aS,aL,aC        

