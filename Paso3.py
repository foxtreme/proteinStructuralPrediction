

import numpy as numeric
#import numpy.oldnumeric.mlab as mlab
from Bio.PDB import *
from os.path import exists

STRUCT_PARSER = PDBParser()#parse a pdb file and returns a structure object
todoslos=list()

"""
para cada proteina en SCOPclassifications.txt que son las que estan en
pdbstyle-2.05/%s/%s.ent se calcula su mapa de distancias y se guarda
en  distanceMaps/distanceMap-(%s).txt
"""


def getCa(struct_file_name, dssp_location,name,name2):

    print struct_file_name


    #domain - the id used for the structure
    #struct_file_name - name of the pdb file
    struct = STRUCT_PARSER.get_structure("domain", struct_file_name) 
    #struct is a collection of model instances
    model = struct.get_list()[0]
    
    #a residue is an aminoacid
    allResidues = list()
    
    for residue in model.get_list()[0]:
        if residue.has_id('CA'):#if it is the name of the atom - carbon atom   
            allResidues.append(residue)

    
    print 'len(allResidues)=%d'%len(allResidues)                    

    matrix = list() 

    maximaDistancia=20.0 

    print '------------1 (calculating distances)'
    
    #square matrix fill with zeros of size len(allResidues)
    answer1 = numeric.zeros((len(allResidues), len(allResidues)), numeric.int) 
    answer2 = numeric.zeros((len(allResidues), len(allResidues)), numeric.float)

    I=0
    J=0
    for I in range(len(allResidues)):
        row = list()
        A=allResidues[I]
        for J in range(len(allResidues)):            
            B=allResidues[J]
            corA= A['CA'].get_coord()#return atomic coordinates
            corB= B['CA'].get_coord()#return atomic coordinates
            distance = numeric.sqrt(numeric.sum((corA-corB)**2))#distance between coordinates
            if distance>maximaDistancia:
                distance=maximaDistancia

            answer2[I,J]=distance
            if distance<=8.0:
                distance=1
            else:
                distance=2
            row.append(distance)
            answer1[I,J]=distance
            
        matrix.append(row) 

    numeric.savetxt('distanceMaps/distanceMap-(%s).txt'%name,answer2,fmt='%f')      
    return 1


f = open('SCOPclassifications.txt','r')
lines = f.readlines()
f.close()

contador=0
todoslos=list()
todoslos2=list()
    
for x in lines:
    y=x.split()[0]
    name=y[1:len(x)]
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
    directory=x[2:4]
    name=x
    filename="pdbstyle-2.05/%s/%s.ent"%(directory,name)
    pair=list()
    pair.append(filename)
    pair.append(name)    
    todoslosdominios.append(pair)

maximo=0
indice=0
for domain in todoslosdominios:
    contador=contador+1
    struct_filename = domain[0]#file path
    name=domain[1]#protein name
    name2=todoslos2[indice]#protein name without g->d modification
    indice=indice+1
    getCa(struct_filename, "dsspcmbi", name,name2)
    
    print "-------%d"%contador
    print "-------%s"%name
