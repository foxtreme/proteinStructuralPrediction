
import numpy as numeric
#import numpy.oldnumeric.mlab as mlab
from Bio.PDB import *

"""
lee los translated/translated-(name).txt
escribe los perfiles profiles/profles-(name).txt   sin normalizar
"""

M=100 

todoslosdominios=list()

f = open('SCOPclassifications.txt','r')
lines = f.readlines()
f.close()

for x in lines:
    y=x.split()[0]
    directory=y[3:5]
    name=y[1:len(y)]

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

    todoslosdominios.append(name) 

losConteos=dict()

for name in todoslosdominios: 
    print name
    f = open('translated/translated-(%s).txt'%(name),'r')    
    lines = f.readlines()
    f.close()

    count = list()
    for x in range(M):
        count.append(0)
    for l in lines: 
        d=l.split()
        total=len(d)
        for x in d:
            valor=int(x)
            count[valor-1]=count[valor-1]+1            

    losConteos[name]=count
    E=losConteos[name]
    file1 = file('profiles/profiles-(%s).txt'%name,'w')
    file1.write(" ".join(["%d" % x for x in E])) 
    file1.close()

