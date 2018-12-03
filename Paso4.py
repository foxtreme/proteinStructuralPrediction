
import numpy as numeric
#import numpy.oldnumeric.mlab as mlab
from Bio.PDB import *

"""
Para las proteinas que hay en randomProteins.txt (que son 100), se calcula
su mapa de distancias y se sacan submatrices de 10x10, estas submatrices que
hay para cada proteina se escriben en clustering/training-subs-(%s).R
es decir, salen 100 archivos R

hay que abrir R y ejecutar los archivos clustering/training-subs-(%s).R
eso crear los archivos medoids-(name,i) para i=1 hasta 50, es decir, los 50
medoides por cada proteina
"""

STRUCT_PARSER = PDBParser()

def getCa(struct_file_name, dssp_location,name):
    #obtains the structure of a given protein
    struct = STRUCT_PARSER.get_structure("domain", struct_file_name)    
    #gets a copy of the model, crystal structures mostly have only 1 model
    model = struct.get_list()[0]   
    allResidues = list()
    allResidues1 = list()
    
    for residue in model.get_list()[0]:    
        if residue.has_id('CA'):
            allResidues.append(residue)
            allResidues1.append(residue.resname) 
            
   
    print 'len(allResidues)=%d'%len(allResidues)                    

    matrix = list() 
    maximaDistancia=20.0 

    for A in allResidues:
        row = list()
        for B in allResidues:
            corA= A['CA'].get_coord()
            corB= B['CA'].get_coord()
            distance = numeric.sqrt(numeric.sum((corA-corB)**2))
            if distance>maximaDistancia:
                distance=maximaDistancia
            row.append(distance)
        matrix.append(row) 
	
    allSubmatrices=list()
    for i in range(len(matrix)-9): 
        for j in range(len(matrix)-9):           
            submatrix = list()
	    #here the 10x10 submatrix is defined
            for k in range(i,i+10):
                for l in range(j,j+10):                    
                    submatrix.append(matrix[k][l])           
            allSubmatrices.append(submatrix)                 

    # to run in R language
    print "writing training-subs-(%s).R"%name
    file1 = file('clustering/training-subs-(%s).R'%name,'w')   
    file1.write("library(cluster)\n")
    file1.write("x = matrix(c(")

    #here are all the submatrices for a given protein
    for i in range(len(allSubmatrices)):
        matrix = allSubmatrices[i] #a submatrix
        unaMatrix=''
        for datos in range(100):#just puts in a line every data of the submatrix
            if i==(len(allSubmatrices)-1) and datos==(100-1):
                unaMatrix=unaMatrix + "%.2f"%matrix[datos]                 
            else:
                unaMatrix=unaMatrix + "%.2f"%matrix[datos] + ","

        file1.write("%s"%unaMatrix) #puts together all the submatrices for a protein

    file1.write("), byrow=TRUE, ncol=100)\n")
    file1.write("pamy <- clara(x,50)\n")
    file1.write("z = pamy$medoids\n")
    #creates the 50 medoid files for every protein
    for i in range(1,50+1):
        file1.write("m%d <- z[%d,]\n"%(i,i))
        file1.write("write(m%d,\"medoids-(%s,%d).txt\",sep=\" \")\n"%(i,name,i))
    file1.close()
    
    return "source(\"training-subs-(%s).R\")\n"%name

todoslosdominios=list()
todoslos=list()

f = open('randomProteins.txt','r')
lines = f.readlines()
f.close()

#lists all the random proteins
for x in lines:
    y=x[0:len(x)-1]
    y= ">" + y
    todoslos.append(y)

#lists all the file paths to the proteins
for x in todoslos:
    
    directory=x[3:5]
    name=x[1:len(x)]    
    filename="pdbstyle-2.05/%s/%s.ent"%(directory,name)
    pair=list()
    pair.append(filename)
    pair.append(name)
    todoslosdominios.append(pair)

source=""

maximo=0
for domain in todoslosdominios: 
    struct_filename = domain[0]
    name=domain[1]
    one=getCa(struct_filename, "dsspcmbi", name)
    source=source+one

file1 = file('clustering/toCLUSTER.R','w')   
file1.write(source)
file1.close()

