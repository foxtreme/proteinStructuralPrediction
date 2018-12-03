
import os.path
import numpy as numeric
#import numpy.oldnumeric.mlab as mlab
from Bio.PDB import *

"""
lee las proteinas que hay en SCOPcomplete.txt e imprime cuales
no estan en pdbstyle-2.05/%s/%s.ent
Luego cambio SCOPcomplete.txt eliminando las que no estan, por ejemplo,
en 2.05 hay 32 proteinas que no estan
"""
#cargo los archivos de texto
f = open('SCOPcomplete.txt','r')
lines = f.readlines()
f.close()

f1 = open('randomUnfiltered.txt','r')
random = f1.readlines()
f1.close()

todoslosnombres=list() #these are the protein names switching the 'g's for 'd's
todaslasclasificaciones=list() #only classifications
todoslosdatos=list() #copy of lines
randomProteins=list() #ordered list of random proteins

#list every SCOP proteins
for x in lines:
    y=x.split()[0]
    name=y[1:len(y)]
    classification=x.split()[1] 
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

    todoslosnombres.append(name)
    todaslasclasificaciones.append(classification)
    todoslosdatos.append("%s %s"%(name,classification))

todoslosdominios=list()#contains the file paths of the proteins in  SCOPcomplete

#creating the list with the paths
for x in todoslosnombres:
    directory=x[2:4]#the directory name is always the 3 & 4 letters of the protein name
    name=x
    filename="pdbstyle-2.05/%s/%s.ent"%(directory,name)
    pair=list()
    pair.append(filename)
    pair.append(name)    
    todoslosdominios.append(pair)

#check for missing files
existenScop=list()
existenRandom=list()
noexistenScop=list()
noexistenRandom=list()

fileRandomProteins = file ('randomProteins.txt','w')
fileSCOPclassifications = file ('SCOPclassifications.txt','w')

#lists the random proteins and create the file randomProteins.txt
for x in random:
    name = x[0:7]
    directory = x[2:4]
    fileroute="pdbstyle-2.05/%s/%s.ent"%(directory,name)
    if os.path.exists(fileroute):
        existenRandom.append(name)
        fileRandomProteins.write("%s\n"%name)
    else:
        noexistenRandom.append(name)
        
fileRandomProteins.close()
    
#tells which SCOP proteins are missing and which aren't
for domain in todoslosdominios:
    struct_filename = domain[0]
    name=domain[1]
    if os.path.exists(struct_filename):
        existenScop.append(struct_filename)
    else:
        noexistenScop.append(name)
        index = todoslosnombres.index(name)#index of the missing protein
        classification = todaslasclasificaciones[index]#protein classification 
        s='%s %s'%(name,classification)
        index2 = todoslosdatos.index(s)#index of the protein with classification
        del todoslosdatos[index2]#deletes the protein from the complete list
        


for x in todoslosdatos:
    fileSCOPclassifications.write(">%s\n"%x)
fileSCOPclassifications.close()

print "proteinas encontradas en SCOPclassifications %s"%(len(existenScop))
print "no se encontraron %s proteinas "%(len(noexistenScop))


    


