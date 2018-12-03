# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 19:33:49 2016
creates the training dataset to use in weka
training ONLY
@author: Chris
"""
import random
#load all proteins and their classification
f1 = open("SCOPclassifications.txt","r")
lines = f1.readlines()
f1.close()
#quantity of each class
counter = 0
classA = list()
classB = list()
classC = list()
classD = list()
classE = list()
classF = list()
classG = list()

#name and class
#create lists with both
for x in lines:
    y = x.split()[0]
    name = y[1:len(y)]
    z = x.split()[1]
    classification = z[0:1]
    if classification == 'a':
        pair = list()
        pair.append(name)
        pair.append(classification)
        classA.append(pair)
    elif classification == 'b':
        pair = list()
        pair.append(name)
        pair.append(classification)
        classB.append(pair)
    elif classification == 'c':
        pair = list()
        pair.append(name)
        pair.append(classification)
        classC.append(pair)
    elif classification == 'd':
        pair = list()
        pair.append(name)
        pair.append(classification)
        classD.append(pair)
    elif classification == 'e':
        pair = list()
        pair.append(name)
        pair.append(classification)
        classE.append(pair)
    elif classification == 'f':
        pair = list()
        pair.append(name)
        pair.append(classification)
        classF.append(pair)
    elif classification == 'g':
        pair = list()
        pair.append(name)
        pair.append(classification)
        classG.append(pair)

   
print "classA: %d, classB: %d, classC: %d, classD: %d, classE: %d, classF: %d, classG: %d"%(len(classA),len(classB),len(classC),len(classD),len(classE),len(classF),len(classG))
print "total: %d"%(len(classA)+len(classB)+len(classC)+len(classD)+len(classE)+len(classF)+len(classG))

#header of the training file
f2 = file("sources/class_level/trainingDataset-full.arff","w")
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
f2.write("@ATTRIBUTE class {1,2,3,4,5,6,7}\n")
f2.write("@DATA\n")

#number of proteins to be used in the traning
trainSizeA = len(classA)

trainSizeB = len(classB)

trainSizeC = len(classC)

trainSizeD = len(classD)

trainSizeE = len(classE)

trainSizeF = len(classF)

trainSizeG = len(classG)


#now for the 80% of proteins in SCOPclassifications we create the training row

index = 0
thisName = ""
thisClass = ""
#class A distribution
for i in range(trainSizeA):
    idx = random.randint(0,(len(classA)-1))
    protein = classA[idx]#choose a random protein
    thisName = protein[0]
    thisClass = "1"     
    f = open("normalized/normalized-profile-(%s).txt"%thisName,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,thisClass))
    del classA[idx]#remove the used protein from the list
#class B distribution
for i in range(trainSizeB):
    idx = random.randint(0,(len(classB)-1))
    protein = classB[idx]#choose a random protein
    thisName = protein[0]
    thisClass = "2"     
    f = open("normalized/normalized-profile-(%s).txt"%thisName,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,thisClass))
    del classB[idx]#remove the used protein from the list
#class C distribution    
for i in range(trainSizeC):
    idx = random.randint(0,len(classC)-1)
    protein = classC[idx]#choose a random protein
    thisName = protein[0]
    thisClass = "3"     
    f = open("normalized/normalized-profile-(%s).txt"%thisName,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,thisClass))
    del classC[idx]#remove the used protein from the list
#class D distribution
for i in range(trainSizeD):
    idx = random.randint(0,len(classD)-1)
    protein = classD[idx]#choose a random protein
    thisName = protein[0]
    thisClass = "4"     
    f = open("normalized/normalized-profile-(%s).txt"%thisName,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,thisClass))
    del classD[idx]#remove the used protein from the list
#class E distribution
for i in range(trainSizeE):
    idx = random.randint(0,len(classE)-1)
    protein = classE[idx]#choose a random protein
    thisName = protein[0]
    thisClass = "5"     
    f = open("normalized/normalized-profile-(%s).txt"%thisName,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,thisClass))
    del classE[idx]#remove the used protein from the list
#class F distribution
for i in range(trainSizeF):
    idx = random.randint(0,len(classF)-1)
    protein = classF[idx]#choose a random protein
    thisName = protein[0]
    thisClass = "6"     
    f = open("normalized/normalized-profile-(%s).txt"%thisName,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,thisClass))
    del classF[idx]#remove the used protein from the list
#class G distribution
for i in range(trainSizeG):
    idx = random.randint(0,len(classG)-1)
    protein = classG[idx]#choose a random protein
    thisName = protein[0]
    thisClass = "7"     
    f = open("normalized/normalized-profile-(%s).txt"%thisName,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,thisClass))
    del classG[idx]#remove the used protein from the list
f2.close()    

print "trainSizeA: %d -- "%(trainSizeA)
print "trainSizeB: %d -- "%(trainSizeB)
print "trainSizeC: %d -- "%(trainSizeC)
print "trainSizeD: %d -- "%(trainSizeD)
print "trainSizeE: %d -- "%(trainSizeE)
print "trainSizeF: %d -- "%(trainSizeF)
print "trainSizeG: %d -- "%(trainSizeG)
