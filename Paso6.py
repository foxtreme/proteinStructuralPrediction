import numpy as numeric
#import numpy.oldnumeric.mlab as mlab
from Bio.PDB import *
from os.path import exists
import scipy.spatial

"""
carga los 100 modelos de clustering/100MEDOIDS-%d.txt
carga el archivo con el mapa de distancia distanceMaps/distanceMap-(name).txt
calcula el perfil para cada proteina translated/translated-(name).txt
"""

medoids3D=list()

#makes a list with 100 medoids, each value contains the 100 values of each medoid
def getMedoids3D():
    for m in range(1,100+1): 
        f = open('clustering/100MEDOIDS-%d.txt'%(m),'r')
        lines = f.readlines()
        f.close()

        unMedoid=list()
        valores=""
        for l in range(0,19+1):            
            d=lines[l].split()
            unMedoid.append(float(d[0]))
            unMedoid.append(float(d[1]))
            unMedoid.append(float(d[2]))
            unMedoid.append(float(d[3]))
            unMedoid.append(float(d[4]))

        medoids3D.append(unMedoid)
    return 1

def getCa(struct_file_name, dssp_location,name,name2):

    answer1=numeric.loadtxt('distanceMaps/distanceMap-(%s).txt'%name)
    longitud=len(answer1) 
        
    translated=list()    
    submatrices=list()

    for i in range(longitud-9): 
        for j in range(longitud-9):             
            submatrix1 = answer1[i:i+10,j:j+10]
            p1=sum(submatrix1.tolist(),[])
            submatrices.append(p1)

    #Computes euclidean distance between each pair of the two collections of inputs.            
    nuevo1 = scipy.spatial.distance.cdist(submatrices,medoids3D,'euclidean')
    
    for pos in range(len(nuevo1)):
        tupla1=nuevo1[pos]
        indiceMenor=tupla1.argmin()+1                    
        translated.append(indiceMenor)
        
    print len(translated)
    file1 = file('translated/translated-(%s).txt'%name,'w')
    file1.write(" ".join(["%d" % x for x in translated])) 
    file1.close()

todoslos=list()

f = open('SCOPclassifications.txt','r')
lines = f.readlines()
f.close()

contador=0
todoslos=list()
todoslos2=list()
    
for x in lines:
    y=x.split()[0]
    directory=y[3:5]
    name=y[1:len(y)]
    todoslos2.append(name)
  
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
   
    todoslos.append(name)


todoslosdominios=list()

for x in todoslos:       
    directory=x[3:5]
    name=x   
    filename="pdbstyle-1.75/%s/%s.ent"%(directory,name)
    pair=list()
    pair.append(filename)
    pair.append(name)   
    todoslosdominios.append(pair)

getMedoids3D()

maximo=0
indice=0
for domain in todoslosdominios:  
    contador=contador+1
    struct_filename = domain[0]
    name=domain[1]
    name2=todoslos2[indice]
    indice=indice+1
    getCa(struct_filename, "dsspcmbi", name,name2)
    print "-------%d"%contador
    print "-------%s"%name

