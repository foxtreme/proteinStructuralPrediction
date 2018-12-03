
import random
import numpy as numeric
#import numpy.oldnumeric.mlab as mlab
#from Bio.PDB import *

"""
recibe 'scop205-sequences.txt' que es el archivo que se toma del ASTRAL
escribe SCOPcomplete.txt con los nombres de las proteinas y su clasificacion SCOP
escribe randomUnfiltered.txt con los nombres de las proteinas seleccionadas al azar
"""

todoslosdominios=list()

f = open('scop205-sequences.txt','r')
lines = f.readlines()
f.close()

todosNames=list() 
todosSCOP=list() 

totalDomains=0
for x in lines:

    if x.find('>')==0:#at the beggining of the string

        totalDomains=totalDomains+1
        
        n=x.split()[0]
        name=n[1:len(n)] #removes the '>'
        todosNames.append(name)# protein name
        y=x.split()[1] 
        todosSCOP.append(y)# protein classification


print "TOTAL DOMAINS = %d"%len(todosNames)

file1 = file('SCOPcomplete.txt','w')   

for i in range(len(todosNames)):
    n=todosNames[i]
    c=todosSCOP[i]    
    s=">%s %s"%(n,c)
    file1.write("%s\n"%s)

file1.close()


randomlySelected=list()
for i in range(100):
    x=random.randint(0,len(todosNames))
    randomlySelected.append(todosNames[x])

file1 = file('randomUnfiltered.txt','w') # contains 100 proteins randomly picked 

for i in range(len(randomlySelected)):
    file1.write("%s\n"%(randomlySelected[i]))

file1.close()



