# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 19:33:49 2016
Lists the selected proteins to use in fold classification
creates the training and testing datasets
to use in weka, WITH class and fold verification
100% for training ONLY
@author: Chris
"""
import random
#load all proteins and their classification
f1 = open("SCOPclassifications.txt","r")
lines = f1.readlines()
f1.close()
#quantity of each class, lists are used for different elements recount
foldA = list()
foldB = list()
foldC = list()
foldD = list()
foldE = list()
foldF = list()
foldG = list()
#list of name and fold by class
foldAProteins = list()
foldBProteins = list()
foldCProteins = list()
foldDProteins = list()
foldEProteins = list()
foldFProteins = list()
foldGProteins = list()
#to quickly access the proteins and classifications
SCOP = dict()
#name and class
#create lists with both
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

    #counting folds in class
    if(class_only == 'a'):
        foldA.append(fold_only)
        foldAProteins.append(pair)
    elif(class_only == 'b'):
        foldB.append(fold_only)
        foldBProteins.append(pair)
    elif(class_only == 'c'):
        foldC.append(fold_only)
        foldCProteins.append(pair)
    elif(class_only == 'd'):
        foldD.append(fold_only)
        foldDProteins.append(pair)
    elif(class_only == 'e'):
        foldE.append(fold_only)
        foldEProteins.append(pair)
    elif(class_only == 'f'):
        foldF.append(fold_only)
        foldFProteins.append(pair)
    elif(class_only == 'g'):
        foldG.append(fold_only)
        foldGProteins.append(pair)

#to count different folds only
a = len(set(foldA))
b = len(set(foldB))
c = len(set(foldC))
d = len(set(foldD))
e = len(set(foldE))
f = len(set(foldF))
g = len(set(foldG))
minimum = min(a,b,c,d,e,f,g)#common to all
print "foldsA: %d, foldsB: %d, foldsC: %d, foldsD: %d, foldsE: %d, foldsF: %d, foldsG: %d"%(a,b,c,d,e,f,g)
print "common folds: %d"%minimum

#header of the training file
f2 = file("sources/fold_level/trainingDataset-fold1.arff","w")
f2.write("%1. Title: Normalized Profiles\n")
f2.write("%2. Sources:\n")
f2.write("%\t\t(a) Creator: Christian Charry\n")
f2.write("%\t\t(b) Date: October 2016\n")
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
f2.write("@ATTRIBUTE class STRING\n")
f2.write("@DATA\n")

f3 = file("sources/fold_level/selectedProteins-fold1.txt","w")
#name of the protein in class %
#fold of the protein in class %
nameFoldATemp = ""
foldATemp = ""
nameFoldBTemp = ""
foldBTemp = ""
nameFoldCTemp = ""
foldCTemp = ""
nameFoldDTemp = ""
foldDTemp = ""
nameFoldETemp = ""
foldETemp = ""
nameFoldFTemp = ""
foldFTemp = ""
nameFoldGTemp = ""
foldGTemp = ""
minFold = 1
index = 0
#class A folds
while(minFold<minimum):
    nameFoldATemp = foldAProteins[index][0]
    foldATemp =foldAProteins[index][1]     
    minFold = int(foldATemp.split('.')[1])
    f = open("normalized/normalized-profile-(%s).txt"%nameFoldATemp,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,foldATemp))
    f3.write("%s %s\n"%(">"+nameFoldATemp,SCOP[">"+nameFoldATemp]))
    del foldAProteins[index]#remove the used protein from the list
    index=index+1

#class B folds
minFold = 1
index = 0
while(minFold<minimum):
    nameFoldBTemp = foldBProteins[index][0]
    foldBTemp =foldBProteins[index][1]     
    minFold = int(foldBTemp.split('.')[1])
    f = open("normalized/normalized-profile-(%s).txt"%nameFoldBTemp,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,foldBTemp))
    f3.write("%s %s\n"%(">"+nameFoldBTemp,SCOP[">"+nameFoldBTemp]))
    del foldBProteins[index]#remove the used protein from the list
    index=index+1
#class C folds
minFold = 1
index = 0
while(minFold<minimum):
    nameFoldCTemp = foldCProteins[index][0]
    foldCTemp =foldCProteins[index][1]     
    minFold = int(foldCTemp.split('.')[1])
    f = open("normalized/normalized-profile-(%s).txt"%nameFoldCTemp,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,foldCTemp))
    f3.write("%s %s\n"%(">"+nameFoldCTemp,SCOP[">"+nameFoldCTemp]))
    del foldCProteins[index]#remove the used protein from the list
    index=index+1
#class D folds
minFold = 1
index = 0
while(minFold<minimum):
    nameFoldDTemp = foldDProteins[index][0]
    foldDTemp =foldDProteins[index][1]     
    minFold = int(foldDTemp.split('.')[1])
    f = open("normalized/normalized-profile-(%s).txt"%nameFoldDTemp,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,foldDTemp))
    f3.write("%s %s\n"%(">"+nameFoldDTemp,SCOP[">"+nameFoldDTemp]))
    del foldDProteins[index]#remove the used protein from the list
    index=index+1
#class E folds
minFold = 1
index = 0
while(minFold<minimum):
    nameFoldETemp = foldEProteins[index][0]
    foldETemp =foldEProteins[index][1]     
    minFold = int(foldETemp.split('.')[1])
    f = open("normalized/normalized-profile-(%s).txt"%nameFoldETemp,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,foldETemp))
    f3.write("%s %s\n"%(">"+nameFoldETemp,SCOP[">"+nameFoldETemp]))
    del foldEProteins[index]#remove the used protein from the list
    index=index+1
#class F folds
minFold = 1
index = 0
while(minFold<minimum):
    nameFoldFTemp = foldFProteins[index][0]
    foldFTemp =foldFProteins[index][1]     
    minFold = int(foldFTemp.split('.')[1])
    f = open("normalized/normalized-profile-(%s).txt"%nameFoldFTemp,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,foldFTemp))
    f3.write("%s %s\n"%(">"+nameFoldFTemp,SCOP[">"+nameFoldFTemp]))
    del foldFProteins[index]#remove the used protein from the list
    index=index+1
#class G folds
minFold = 1
index = 0
while(minFold<minimum):
    nameFoldGTemp = foldGProteins[index][0]
    foldGTemp =foldGProteins[index][1]     
    minFold = int(foldGTemp.split('.')[1])
    f = open("normalized/normalized-profile-(%s).txt"%nameFoldGTemp,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,foldGTemp))
    f3.write("%s %s\n"%(">"+nameFoldGTemp,SCOP[">"+nameFoldGTemp]))
    del foldGProteins[index]#remove the used protein from the list
    index=index+1
f2.close()   
f3.close() 
