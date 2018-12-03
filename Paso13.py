# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 19:33:49 2016
creates a training file for CVF testing with the 5th 
selected set for testing and the other 4 sets for training
"""
import random
#load all proteins and their classification - training
f1 = open("sources/class_level/lff5comp.txt","r")
lines = f1.readlines()
f1.close()

#load all proteins and their classification - test
f3 = open("sources/class_level/lff5.txt","r")
lines2 = f3.readlines()
f3.close()
#quantity of each class
counter = 0
#training
training = list()
#test
test = list()

#name and class
#create lists with both
for x in lines:
    y = x.split()[0]
    name = y[1:len(y)]
    z = x.split()[1]
    classification = z[0:1]
    pair = list()
    pair.append(name)
    pair.append(classification)
    training.append(pair)

for x in lines2:
    y = x.split()[0]
    name = y[1:len(y)]
    z = x.split()[1]
    classification = z[0:1]
    pair = list()
    pair.append(name)
    pair.append(classification)
    test.append(pair)

print "Training: %d -- Test: %d"%(len(training) , len(test))
print "total: %d"%(len(training)+len(test))
    
#header of the training file
f2 = file("sources/class_level/trainingDataset-5.arff","w")
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
trainSizeA = len(training)

#now  we create the training row

index = 0
thisName = ""
thisClass = ""
#class A distribution
for i in range(trainSizeA):
    idx = random.randint(0,(len(training)-1))
    protein = training[idx]#choose a random protein
    thisName = protein[0]
    classification = protein[1]     
    if classification == 'a':
        thisClass = "1"
    elif classification == 'b':
        thisClass = "2"
    elif classification == 'c':
        thisClass = "3"
    elif classification == 'd':
        thisClass = "4"
    elif classification == 'e':
        thisClass = "5"
    elif classification == 'f':
        thisClass = "6"
    elif classification == 'g':
        thisClass = "7"
    f = open("normalized/normalized-profile-(%s).txt"%thisName,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,thisClass))
    del training[idx]#remove the used protein from the list

f2.close()    
#header of the training file
f3 = file("sources/class_level/testDataset-5.arff","w")
f3.write("%1. Title: Normalized Profiles\n")
f3.write("%2. Sources:\n")
f3.write("%\t\t(a) Creator: Christian Charry\n")
f3.write("%\t\t(b) Date: October 2016\n")
f3.write("@RELATION NP\n")
#f2.write("@ATTRIBUTE name STRING\n")
f3.write("@ATTRIBUTE p1 REAL\n")
f3.write("@ATTRIBUTE p2 REAL\n")
f3.write("@ATTRIBUTE p3 REAL\n")
f3.write("@ATTRIBUTE p4 REAL\n")
f3.write("@ATTRIBUTE p5 REAL\n")
f3.write("@ATTRIBUTE p6 REAL\n")
f3.write("@ATTRIBUTE p7 REAL\n")
f3.write("@ATTRIBUTE p8 REAL\n")
f3.write("@ATTRIBUTE p9 REAL\n")
f3.write("@ATTRIBUTE p10 REAL\n")
f3.write("@ATTRIBUTE p11 REAL\n")
f3.write("@ATTRIBUTE p12 REAL\n")
f3.write("@ATTRIBUTE p13 REAL\n")
f3.write("@ATTRIBUTE p14 REAL\n")
f3.write("@ATTRIBUTE p15 REAL\n")
f3.write("@ATTRIBUTE p16 REAL\n")
f3.write("@ATTRIBUTE p17 REAL\n")
f3.write("@ATTRIBUTE p18 REAL\n")
f3.write("@ATTRIBUTE p19 REAL\n")
f3.write("@ATTRIBUTE p20 REAL\n")
f3.write("@ATTRIBUTE p21 REAL\n")
f3.write("@ATTRIBUTE p22 REAL\n")
f3.write("@ATTRIBUTE p23 REAL\n")
f3.write("@ATTRIBUTE p24 REAL\n")
f3.write("@ATTRIBUTE p25 REAL\n")
f3.write("@ATTRIBUTE p26 REAL\n")
f3.write("@ATTRIBUTE p27 REAL\n")
f3.write("@ATTRIBUTE p28 REAL\n")
f3.write("@ATTRIBUTE p29 REAL\n")
f3.write("@ATTRIBUTE p30 REAL\n")
f3.write("@ATTRIBUTE p31 REAL\n")
f3.write("@ATTRIBUTE p32 REAL\n")
f3.write("@ATTRIBUTE p33 REAL\n")
f3.write("@ATTRIBUTE p34 REAL\n")
f3.write("@ATTRIBUTE p35 REAL\n")
f3.write("@ATTRIBUTE p36 REAL\n")
f3.write("@ATTRIBUTE p37 REAL\n")
f3.write("@ATTRIBUTE p38 REAL\n")
f3.write("@ATTRIBUTE p39 REAL\n")
f3.write("@ATTRIBUTE p40 REAL\n")
f3.write("@ATTRIBUTE p41 REAL\n")
f3.write("@ATTRIBUTE p42 REAL\n")
f3.write("@ATTRIBUTE p43 REAL\n")
f3.write("@ATTRIBUTE p44 REAL\n")
f3.write("@ATTRIBUTE p45 REAL\n")
f3.write("@ATTRIBUTE p46 REAL\n")
f3.write("@ATTRIBUTE p47 REAL\n")
f3.write("@ATTRIBUTE p48 REAL\n")
f3.write("@ATTRIBUTE p49 REAL\n")
f3.write("@ATTRIBUTE p50 REAL\n")
f3.write("@ATTRIBUTE p51 REAL\n")
f3.write("@ATTRIBUTE p52 REAL\n")
f3.write("@ATTRIBUTE p53 REAL\n")
f3.write("@ATTRIBUTE p54 REAL\n")
f3.write("@ATTRIBUTE p55 REAL\n")
f3.write("@ATTRIBUTE p56 REAL\n")
f3.write("@ATTRIBUTE p57 REAL\n")
f3.write("@ATTRIBUTE p58 REAL\n")
f3.write("@ATTRIBUTE p59 REAL\n")
f3.write("@ATTRIBUTE p60 REAL\n")
f3.write("@ATTRIBUTE p61 REAL\n")
f3.write("@ATTRIBUTE p62 REAL\n")
f3.write("@ATTRIBUTE p63 REAL\n")
f3.write("@ATTRIBUTE p64 REAL\n")
f3.write("@ATTRIBUTE p65 REAL\n")
f3.write("@ATTRIBUTE p66 REAL\n")
f3.write("@ATTRIBUTE p67 REAL\n")
f3.write("@ATTRIBUTE p68 REAL\n")
f3.write("@ATTRIBUTE p69 REAL\n")
f3.write("@ATTRIBUTE p70 REAL\n")
f3.write("@ATTRIBUTE p71 REAL\n")
f3.write("@ATTRIBUTE p72 REAL\n")
f3.write("@ATTRIBUTE p73 REAL\n")
f3.write("@ATTRIBUTE p74 REAL\n")
f3.write("@ATTRIBUTE p75 REAL\n")
f3.write("@ATTRIBUTE p76 REAL\n")
f3.write("@ATTRIBUTE p77 REAL\n")
f3.write("@ATTRIBUTE p78 REAL\n")
f3.write("@ATTRIBUTE p79 REAL\n")
f3.write("@ATTRIBUTE p80 REAL\n")
f3.write("@ATTRIBUTE p81 REAL\n")
f3.write("@ATTRIBUTE p82 REAL\n")
f3.write("@ATTRIBUTE p83 REAL\n")
f3.write("@ATTRIBUTE p84 REAL\n")
f3.write("@ATTRIBUTE p85 REAL\n")
f3.write("@ATTRIBUTE p86 REAL\n")
f3.write("@ATTRIBUTE p87 REAL\n")
f3.write("@ATTRIBUTE p88 REAL\n")
f3.write("@ATTRIBUTE p89 REAL\n")
f3.write("@ATTRIBUTE p90 REAL\n")
f3.write("@ATTRIBUTE p91 REAL\n")
f3.write("@ATTRIBUTE p92 REAL\n")
f3.write("@ATTRIBUTE p93 REAL\n")
f3.write("@ATTRIBUTE p94 REAL\n")
f3.write("@ATTRIBUTE p95 REAL\n")
f3.write("@ATTRIBUTE p96 REAL\n")
f3.write("@ATTRIBUTE p97 REAL\n")
f3.write("@ATTRIBUTE p98 REAL\n")
f3.write("@ATTRIBUTE p99 REAL\n")
f3.write("@ATTRIBUTE p100 REAL\n")
f3.write("@ATTRIBUTE class {1,2,3,4,5,6,7}\n")
f3.write("@DATA\n")

#number of proteins to be used in the traning
testSizeA = len(test)

#now for the 80% of proteins in SCOPclassifications we create the training row

index = 0
thisName = ""
thisClass = ""

for i in range(testSizeA):
    idx = random.randint(0,(len(test)-1))
    protein = test[idx]#choose a random protein
    thisName = protein[0]
    classification = protein[1]     
    if classification == 'a':
        thisClass = "1"
    elif classification == 'b':
        thisClass = "2"
    elif classification == 'c':
        thisClass = "3"
    elif classification == 'd':
        thisClass = "4"
    elif classification == 'e':
        thisClass = "5"
    elif classification == 'f':
        thisClass = "6"
    elif classification == 'g':
        thisClass = "7"    
    f = open("normalized/normalized-profile-(%s).txt"%thisName,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f3.write("%s, %s\n"%(formattedProfile,thisClass))
    del test[idx]#remove the used protein from the list

f3.close()    

