
import numpy as numeric
#import numpy.oldnumeric.mlab as mlab
from Bio.PDB import *

todoslos=list()

"""
lee los 50 medoids para cada proteina  (archivos clustering/medoids-(%s,%i).txt)
y escribe un solo archivo llamado clustering/training-100MEDOIDS.R
luego ejecuto ese archivo en R y asi obtengo los modelos, estos quedan
guardados en clustering/ asi 100MEDOIDS-1.txt hasta 100MEDOIDS-100.txt
"""

f = open('randomProteins.txt','r')

lines = f.readlines()
f.close()
   
for x in lines:
    name=x[0:len(x)-1]
    todoslos.append(name)

file1 = file('clustering/training-100MEDOIDS.R','w')   
file1.write("library(cluster)\n")
file1.write("x = matrix(c(")


print "writing training-100MEDOIDS.R"

cantidad=0
for W in range(len(todoslos)):
    domain=todoslos[W]    
    print domain
    valores=""
    for i in range(1,50+1): #las 50 submatrices por cada proteina
        f = open('clustering/medoids-(%s,%i).txt'%(domain,i),'r')
        lines = f.readlines()
        f.close()

        for j in range(len(lines)):
            cantidad=cantidad+1
            l=lines[j]
            d=l.split()

            if W==len(todoslos)-1 and i==50 and j==len(lines)-1:
                valores=valores + d[0] + ","
                valores=valores + d[1] + ","
                valores=valores + d[2] + ","
                valores=valores + d[3] + ","
                valores=valores + d[4] 
            else:
                valores=valores + d[0] + ","
                valores=valores + d[1] + ","
                valores=valores + d[2] + ","
                valores=valores + d[3] + ","
                valores=valores + d[4] + ","

                   
    file1.write("%s"%valores)

print cantidad
file1.write("), byrow=TRUE, ncol=100)\n")  
file1.write("pamy <- clara(x,100)\n")  
file1.write("z = pamy$medoids\n")
for i in range(1,100+1):
    file1.write("m%d <- z[%d,]\n"%(i,i))
    file1.write("write(m%d,\"100MEDOIDS-%d.txt\",sep=\" \")\n"%(i,i))
file1.close()

