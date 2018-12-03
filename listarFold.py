# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 19:33:49 2016
Lists the selected proteins to use in Superfamily classification
creates the training and testing datasets
to use in weka, WITH class and superfamily verification
100% for training ONLY
@author: Chris
"""
import random
#load all proteins and their classification
f1 = open("SCOPclassifications.txt","r")
lines = f1.readlines()
f1.close()
#quantity of each class, lists are used for different elements recount
foldComplete = list()
#list of name and superfamilies by class
foldCompleteProteins = list()
#to quickly access the proteins and classifications
SCOP = dict()
Fquantification = dict() #keep track of proteins by fold
#name and class
#create lists with both+
biggest_fold = 0#the biggest data in a fold
contador = 0
foldZero = "a.0" #starting fold
max_fold = ""
for x in lines:
    y = x.split()[0]
    name = y[1:len(y)]
    z = x.split()[1]#classification a.1.1.1
    class_only = z.split('.')[0]
    fold_only = z.split('.')[1]    
    fold = class_only+"."+fold_only
    pair = list()
    pair.append(name)
    pair.append(fold)
    SCOP[y] = z
    #keeping track of greatest superfamily
    '''
    if superfamily == superfamilyZero: #si es igual a la anterior 
        contador = contador+1          #incrementa la cuenta
        if contador>biggest_superfamily:
            biggest_superfamily = contador
            max_superfamily = superfamily
    else:                              #si es diferente a la anterior      
        contador = 1
        superfamilyZero = superfamily
    #print "contador: %d --- current superfamily: %s biggest superfamily: %s quatity: %d\n"%(contador,superfamily,max_superfamily,biggest_superfamily)
    #counting folds in class
    '''
    #creates a list of proteins by superfamily
    
    if fold == foldZero:
        contador = contador+1  #si es igual a la anterior incrementa la cuenta y pasa a la siguiente
    else:
        Fquantification[foldZero] = contador
        foldZero = fold
        contador = 1
    
    foldComplete.append(fold_only)
    foldCompleteProteins.append(pair)
    
#print "greatest data size-- superfamily name: %s quatity: %d\n"%(max_superfamily,biggest_superfamily)

selectedFolds = list()
#to select only superfamilies with enough data
print "fold - quantity of proteins %d"%len(Fquantification)
print "============ FILTERED =========="
for x in Fquantification.keys():
    val = Fquantification[x]
    key = x
    if val >= 200:
        print "%s %d"%(x,Fquantification[x])
        selectedFolds.append(x)
print "-------- the folds with more data ----------"
for x in selectedFolds:
    print x
'''
#header of the training file
f2 = file("sources/fold_level/trainingDataset-fold_qt.arff","w")
f2.write("%1. Title: Normalized Profiles\n")
f2.write("%2. Sources:\n")
f2.write("%\t\t(a) Creator: Christian Charry\n")
f2.write("%\t\t(b) Date: April 2017\n")
f2.write("@RELATION NP\n")
#f2.write("@ATTRIBUTE name STRING\n")
f2.write("@ATTRIBUTE p1 REAL\n")
f2.write("@ATTRIBUTE p2 REAL\n")
f2.write("@ATTRIBUTE p3 REAL\n")
f2.write("@ATTRIBUTE p4 REAL\n")
f2.write("@ATTRIBUTE p5 REAL\n")
f2.write("@ATTRIBUTE p6 REAL\n")
f2.write("@ATTRIBUTE p7 REAL\n")
f2.write("@ATTRIBUTE p8 REAL\n")
f2.write("@ATTRIBUTE p9 REAL\n")
f2.write("@ATTRIBUTE p10 REAL\n")
f2.write("@ATTRIBUTE p11 REAL\n")
f2.write("@ATTRIBUTE p12 REAL\n")
f2.write("@ATTRIBUTE p13 REAL\n")
f2.write("@ATTRIBUTE p14 REAL\n")
f2.write("@ATTRIBUTE p15 REAL\n")
f2.write("@ATTRIBUTE p16 REAL\n")
f2.write("@ATTRIBUTE p17 REAL\n")
f2.write("@ATTRIBUTE p18 REAL\n")
f2.write("@ATTRIBUTE p19 REAL\n")
f2.write("@ATTRIBUTE p20 REAL\n")
f2.write("@ATTRIBUTE p21 REAL\n")
f2.write("@ATTRIBUTE p22 REAL\n")
f2.write("@ATTRIBUTE p23 REAL\n")
f2.write("@ATTRIBUTE p24 REAL\n")
f2.write("@ATTRIBUTE p25 REAL\n")
f2.write("@ATTRIBUTE p26 REAL\n")
f2.write("@ATTRIBUTE p27 REAL\n")
f2.write("@ATTRIBUTE p28 REAL\n")
f2.write("@ATTRIBUTE p29 REAL\n")
f2.write("@ATTRIBUTE p30 REAL\n")
f2.write("@ATTRIBUTE p31 REAL\n")
f2.write("@ATTRIBUTE p32 REAL\n")
f2.write("@ATTRIBUTE p33 REAL\n")
f2.write("@ATTRIBUTE p34 REAL\n")
f2.write("@ATTRIBUTE p35 REAL\n")
f2.write("@ATTRIBUTE p36 REAL\n")
f2.write("@ATTRIBUTE p37 REAL\n")
f2.write("@ATTRIBUTE p38 REAL\n")
f2.write("@ATTRIBUTE p39 REAL\n")
f2.write("@ATTRIBUTE p40 REAL\n")
f2.write("@ATTRIBUTE p41 REAL\n")
f2.write("@ATTRIBUTE p42 REAL\n")
f2.write("@ATTRIBUTE p43 REAL\n")
f2.write("@ATTRIBUTE p44 REAL\n")
f2.write("@ATTRIBUTE p45 REAL\n")
f2.write("@ATTRIBUTE p46 REAL\n")
f2.write("@ATTRIBUTE p47 REAL\n")
f2.write("@ATTRIBUTE p48 REAL\n")
f2.write("@ATTRIBUTE p49 REAL\n")
f2.write("@ATTRIBUTE p50 REAL\n")
f2.write("@ATTRIBUTE p51 REAL\n")
f2.write("@ATTRIBUTE p52 REAL\n")
f2.write("@ATTRIBUTE p53 REAL\n")
f2.write("@ATTRIBUTE p54 REAL\n")
f2.write("@ATTRIBUTE p55 REAL\n")
f2.write("@ATTRIBUTE p56 REAL\n")
f2.write("@ATTRIBUTE p57 REAL\n")
f2.write("@ATTRIBUTE p58 REAL\n")
f2.write("@ATTRIBUTE p59 REAL\n")
f2.write("@ATTRIBUTE p60 REAL\n")
f2.write("@ATTRIBUTE p61 REAL\n")
f2.write("@ATTRIBUTE p62 REAL\n")
f2.write("@ATTRIBUTE p63 REAL\n")
f2.write("@ATTRIBUTE p64 REAL\n")
f2.write("@ATTRIBUTE p65 REAL\n")
f2.write("@ATTRIBUTE p66 REAL\n")
f2.write("@ATTRIBUTE p67 REAL\n")
f2.write("@ATTRIBUTE p68 REAL\n")
f2.write("@ATTRIBUTE p69 REAL\n")
f2.write("@ATTRIBUTE p70 REAL\n")
f2.write("@ATTRIBUTE p71 REAL\n")
f2.write("@ATTRIBUTE p72 REAL\n")
f2.write("@ATTRIBUTE p73 REAL\n")
f2.write("@ATTRIBUTE p74 REAL\n")
f2.write("@ATTRIBUTE p75 REAL\n")
f2.write("@ATTRIBUTE p76 REAL\n")
f2.write("@ATTRIBUTE p77 REAL\n")
f2.write("@ATTRIBUTE p78 REAL\n")
f2.write("@ATTRIBUTE p79 REAL\n")
f2.write("@ATTRIBUTE p80 REAL\n")
f2.write("@ATTRIBUTE p81 REAL\n")
f2.write("@ATTRIBUTE p82 REAL\n")
f2.write("@ATTRIBUTE p83 REAL\n")
f2.write("@ATTRIBUTE p84 REAL\n")
f2.write("@ATTRIBUTE p85 REAL\n")
f2.write("@ATTRIBUTE p86 REAL\n")
f2.write("@ATTRIBUTE p87 REAL\n")
f2.write("@ATTRIBUTE p88 REAL\n")
f2.write("@ATTRIBUTE p89 REAL\n")
f2.write("@ATTRIBUTE p90 REAL\n")
f2.write("@ATTRIBUTE p91 REAL\n")
f2.write("@ATTRIBUTE p92 REAL\n")
f2.write("@ATTRIBUTE p93 REAL\n")
f2.write("@ATTRIBUTE p94 REAL\n")
f2.write("@ATTRIBUTE p95 REAL\n")
f2.write("@ATTRIBUTE p96 REAL\n")
f2.write("@ATTRIBUTE p97 REAL\n")
f2.write("@ATTRIBUTE p98 REAL\n")
f2.write("@ATTRIBUTE p99 REAL\n")
f2.write("@ATTRIBUTE p100 REAL\n")
f2.write("@ATTRIBUTE class {c.47 ,c.37,a.4,d.58,b.1,c.23,c.2,c.1}\n")
f2.write("@DATA\n")

f3 = file("sources/fold_level/selectedProteins-fold_qt.txt","w")
#name of the protein in class %
#superfamily of the protein in class %


for x in foldCompleteProteins:
    if x[1] in selectedFolds:
        proteinName = x[0]
        f = open("normalized/normalized-profile-(%s).txt"%proteinName,'r')#open the normalized protein file for the data
        data = f.readline()
        f.close()
        vector = data.split()
        separator = ", "
        formattedProfile = separator.join(vector)#format the lff profile of the protein
        f2.write("%s, %s\n"%(formattedProfile,SCOP[">"+proteinName]))
        f3.write("%s %s\n"%(">"+proteinName,SCOP[">"+proteinName]))    
                        
        
f2.close()   

f3.close() 

'''
