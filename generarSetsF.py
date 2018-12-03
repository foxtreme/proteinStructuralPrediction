# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:36:43 2016
creates the 5 sets to use CVF with the LFF method
@author: Chris
"""
import random
#load all proteins and their classification
f1 = open("sources/family_level/selectedProteins-family_U30.txt","r")
lines = f1.readlines()
f1.close()
#name and class
allProteins = list()
#create list with both
for x in lines:
    y = x.split()[0]
    name = y[1:len(y)]
    z = x.split()[1]
    pair = list()
    pair.append(name)
    pair.append(z)
    allProteins.append(pair)

    f2 = file("sources/family_level/lff1_U30.txt","w")
    f3 = file("sources/family_level/lff2_U30.txt","w")
    f4 = file("sources/family_level/lff3_U30.txt","w")
    f5 = file("sources/family_level/lff4_U30.txt","w")
    f6 = file("sources/family_level/lff5_U30.txt","w")
    
for i in range(406):#quantity of selected proteins/5
    #file 2
    idx = random.randint(0,len(allProteins)-1)
    protein = allProteins[idx]
    name = protein[0]
    family = protein[1]
    f2.write(">%s %s\n"%(name,family))
    del allProteins[idx]
    #file 3
    idx = random.randint(0,len(allProteins)-1)
    protein = allProteins[idx]
    name = protein[0]
    family = protein[1]
    f3.write(">%s %s\n"%(name,family))
    del allProteins[idx]
    #file 4
    idx = random.randint(0,len(allProteins)-1)
    protein = allProteins[idx]
    name = protein[0]
    family = protein[1]
    f4.write(">%s %s\n"%(name,family))
    del allProteins[idx]
    #file 5
    idx = random.randint(0,len(allProteins)-1)
    protein = allProteins[idx]
    name = protein[0]
    family = protein[1]
    f5.write(">%s %s\n"%(name,family))
    del allProteins[idx]
    #file 6
    idx = random.randint(0,len(allProteins)-1)
    protein = allProteins[idx]
    name = protein[0]
    family = protein[1]
    f6.write(">%s %s\n"%(name,family))
    del allProteins[idx]
'''
#file 2
idx = random.randint(0,len(allProteins)-1)
protein = allProteins[idx]
name = protein[0]
family = protein[1]
f2.write(">%s %s\n"%(name,family))
del allProteins[idx]
'''
f2.close()  
f3.close()  
f4.close()  
f5.close()  
f6.close()  
