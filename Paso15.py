# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:36:43 2016
creates the 5 sets to use CVF with the LFF method
@author: Chris
"""
import random
#load all proteins and their classification
f1 = open("sources/fold_level/selectedProteins-fold_qt.txt","r")
lines = f1.readlines()
f1.close()
#name and class
allProteins = list()
#create list with both
for x in lines:
    y = x.split()[0]
    name = y[1:len(y)]
    z = x.split()[1]
    #class_only = z.split('.')[0]
    #fold_only = z.split('.')[1]    
    #fold = class_only+"."+fold_only
    pair = list()
    pair.append(name)
    pair.append(z)
    allProteins.append(pair)

    f2 = file("sources/fold_level/lff1_qt.txt","w")
    f3 = file("sources/fold_level/lff2_qt.txt","w")
    f4 = file("sources/fold_level/lff3_qt.txt","w")
    f5 = file("sources/fold_level/lff4_qt.txt","w")
    f6 = file("sources/fold_level/lff5_qt.txt","w")
    
for i in range(554):
    #file 2
    idx = random.randint(0,len(allProteins)-1)
    protein = allProteins[idx]
    name = protein[0]
    fold = protein[1]
    f2.write(">%s %s\n"%(name,fold))
    del allProteins[idx]
    #file 3
    idx = random.randint(0,len(allProteins)-1)
    protein = allProteins[idx]
    name = protein[0]
    fold = protein[1]
    f3.write(">%s %s\n"%(name,fold))
    del allProteins[idx]
    #file 4
    idx = random.randint(0,len(allProteins)-1)
    protein = allProteins[idx]
    name = protein[0]
    fold = protein[1]
    f4.write(">%s %s\n"%(name,fold))
    del allProteins[idx]
    #file 5
    idx = random.randint(0,len(allProteins)-1)
    protein = allProteins[idx]
    name = protein[0]
    fold = protein[1]
    f5.write(">%s %s\n"%(name,fold))
    del allProteins[idx]
    #file 6
    idx = random.randint(0,len(allProteins)-1)
    protein = allProteins[idx]
    name = protein[0]
    fold = protein[1]
    f6.write(">%s %s\n"%(name,fold))
    del allProteins[idx]
#file 2
idx = random.randint(0,len(allProteins)-1)
protein = allProteins[idx]
name = protein[0]
fold = protein[1]
f2.write(">%s %s\n"%(name,fold))
del allProteins[idx]
#file 3
idx = random.randint(0,len(allProteins)-1)
protein = allProteins[idx]
name = protein[0]
fold = protein[1]
f3.write(">%s %s\n"%(name,fold))
del allProteins[idx]    

f2.close()  
f3.close()  
f4.close()  
f5.close()  
f6.close()  
