

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

f = open('SCOPclassifications.txt','r')
lines = f.readlines()
f.close()

for x in lines:
    y=x.split()[0]#name with '>'
    directory=y[3:5]#folder of protein
    name=y[1:len(y)]#name of protein
    clase=x.split()[1]#classification
    
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

#for every protein
for name in todoslosdominios:
    f = open('normalized/normalized-profile-(%s).txt'%(name),'r')    
    lines = f.readlines()
    f.close()

    count = list()

    for l in lines:
        d=l.split()#list of values for vector
        #every normalized valor of the vector (100)
        for x in d: 
            valor=float(x) #every valor is a real
            count.append(valor) #add the valor to the count list
    #for every protein, relate its count of 100 values
    losConteos[name]=count


predicciones=list()
for i in range(len(todoslosdominios)):#for every protein
    print i#the number
    nombre1=todoslosdominios[i]
    distancias=list()
    
    for j in range(len(todoslosdominios)):#all vs all

        if i!=j:#if the proteins are different
            name1=todoslosdominios[i]#the outer loop protein
            name2=todoslosdominios[j]#the inner loop protein
            valores1=losConteos[name1]#the vector of the outer loop protein
            valores2=losConteos[name2]#the vector of the inner loop protein

            myarray1 = numeric.asarray(valores1) #convert to array outer vector
            myarray2 = numeric.asarray(valores2) # convert to array inner vector
            ax1=sum(myarray1*myarray1) #squared outer array
            ax2=sum(myarray2*myarray2) #squared inner array       
            cos=sum(myarray1*myarray2)/math.sqrt(ax1*ax2) 
            distancia=1-cos #distance between outer and inner protein [0,1]
            distancias.append(distancia)
        if i==j:#if the proteins are the same
            distancias.append(2) # para que no escoja el mismo

   
    v=numeric.asarray(distancias)#make an array of distances
    menor=v.argmin() #chooses the index of the lesser of them all
    dominioSimilar=todoslosdominios[menor]#protein closest to outer protein
    clase1=scop[nombre1]#class of outer protein
    clasePredicha=scop[dominioSimilar]#class of inner protein
        
    tupla=list()
    tupla.append(clase1)
    tupla.append(clasePredicha)
    predicciones.append(tupla)

aF=0#family
aS=0#superfamily
aL=0#fold
aC=0#class

#conteo de clases
aAsa=0
aAsb=0
aAsc=0
aAsd=0
aAse=0
aAsf=0
aAsg=0

bAsa=0
bAsb=0
bAsc=0
bAsd=0
bAse=0
bAsf=0
bAsg=0

cAsa=0
cAsb=0
cAsc=0
cAsd=0
cAse=0
cAsf=0
cAsg=0

dAsa=0
dAsb=0
dAsc=0
dAsd=0
dAse=0
dAsf=0
dAsg=0

eAsa=0
eAsb=0
eAsc=0
eAsd=0
eAse=0
eAsf=0
eAsg=0

fAsa=0
fAsb=0
fAsc=0
fAsd=0
fAse=0
fAsf=0
fAsg=0

gAsa=0
gAsb=0
gAsc=0
gAsd=0
gAse=0
gAsf=0
gAsg=0

for x in predicciones:
    scop1=x[0]#real class
    scop2=x[1]#foresaw class
    s1=scop1.split(".")
    s2=scop2.split(".")
    super1=s1[0] + "." + s1[1] + "." + s1[2]
    super2=s2[0] + "." + s2[1] + "." + s2[2]    
    fold1=s1[0] + "." + s1[1]
    fold2=s2[0] + "." + s2[1]
    class1=s1[0] 
    class2=s2[0] 

    if class1 == "a":
        if class2 == "a":
            aAsa = aAsa+1
        elif class2 == "b":
            aAsb = aAsb+1
        elif class2 == "c":
            aAsc = aAsc+1
        elif class2 == "d":
            aAsd = aAsd+1
        elif class2 == "e":
            aAse = aAse+1
        elif class2 == "f":
            aAsf = aAsf+1
        elif class2 == "g":
            aAsg = aAsg+1
            
    if class1 == "b":
        if class2 == "a":
            bAsa = bAsa+1
        elif class2 == "b":
            bAsb = bAsb+1
        elif class2 == "c":
            bAsc = bAsc+1
        elif class2 == "d":
            bAsd = bAsd+1
        elif class2 == "e":
            bAse = bAse+1
        elif class2 == "f":
            bAsf = bAsf+1
        elif class2 == "g":
            bAsg = bAsg+1
            
    if class1 == "c":
        if class2 == "a":
            cAsa = cAsa+1
        elif class2 == "b":
            cAsb = cAsb+1
        elif class2 == "c":
            cAsc = cAsc+1
        elif class2 == "d":
            cAsd = cAsd+1
        elif class2 == "e":
            cAse = cAse+1
        elif class2 == "f":
            cAsf = cAsf+1
        elif class2 == "g":
            cAsg = cAsg+1
            
    if class1 == "d":
        if class2 == "a":
            dAsa = dAsa+1
        elif class2 == "b":
            dAsb = dAsb+1
        elif class2 == "c":
            dAsc = dAsc+1
        elif class2 == "d":
            dAsd = dAsd+1
        elif class2 == "e":
            dAse = dAse+1
        elif class2 == "f":
            dAsf = dAsf+1
        elif class2 == "g":
            dAsg = dAsg+1
            
    if class1 == "e":
        if class2 == "a":
            eAsa = eAsa+1
        elif class2 == "b":
            eAsb = eAsb+1
        elif class2 == "c":
            eAsc = eAsc+1
        elif class2 == "d":
            eAsd = eAsd+1
        elif class2 == "e":
            eAse = eAse+1
        elif class2 == "f":
            eAsf = eAsf+1
        elif class2 == "g":
            eAsg = eAsg+1
            
    if class1 == "f":
        if class2 == "a":
            fAsa = fAsa+1
        elif class2 == "b":
            fAsb = fAsb+1
        elif class2 == "c":
            fAsc = fAsc+1
        elif class2 == "d":
            fAsd = fAsd+1
        elif class2 == "e":
            fAse = fAse+1
        elif class2 == "f":
            fAsf = fAsf+1
        elif class2 == "g":
            fAsg = fAsg+1
            
    if class1 == "g":
        if class2 == "a":
            gAsa = gAsa+1
        elif class2 == "b":
            gAsb = gAsb+1
        elif class2 == "c":
            gAsc = gAsc+1
        elif class2 == "d":
            gAsd = gAsd+1
        elif class2 == "e":
            gAse = gAse+1
        elif class2 == "f":
            gAsf = gAsf+1
        elif class2 == "g":
            gAsg = gAsg+1

    if scop1==scop2:
        aF=aF+1
    if super1==super2:
        aS=aS+1
    if fold1==fold2:
        aL=aL+1
    if class1==class2:
        aC=aC+1
#summary = file("summary,txt","w")
print "Family , Superfamily, Fold , Class"
print "%d\t\t%d\t%d\t%d"%(aF,aS,aL,aC)

print "===== confusion matrix ======"
print "\t a\t b\t c\t d\t e\t f\t g\t  <-- classified as"
print "\t%d\t%d\t%d\t%d\t%d\t%d\t%d"%(aAsa,aAsb,aAsc,aAsd,aAse,aAsf,aAsg)
print "\t%d\t%d\t%d\t%d\t%d\t%d\t%d"%(bAsa,bAsb,bAsc,bAsd,bAse,bAsf,bAsg)
print "\t%d\t%d\t%d\t%d\t%d\t%d\t%d"%(cAsa,cAsb,cAsc,cAsd,cAse,cAsf,cAsg)
print "\t%d\t%d\t%d\t%d\t%d\t%d\t%d"%(dAsa,dAsb,dAsc,dAsd,dAse,dAsf,dAsg)
print "\t%d\t%d\t%d\t%d\t%d\t%d\t%d"%(eAsa,eAsb,eAsc,eAsd,eAse,eAsf,eAsg)
print "\t%d\t%d\t%d\t%d\t%d\t%d\t%d"%(fAsa,fAsb,fAsc,fAsd,fAse,fAsf,fAsg)
print "\t%d\t%d\t%d\t%d\t%d\t%d\t%d"%(gAsa,gAsb,gAsc,gAsd,gAse,gAsf,gAsg)
