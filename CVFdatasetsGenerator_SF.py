# -*- coding: utf-8 -*-
"""
Created on May 2017
creates a training file for CVF testing with the 5th 
selected set for testing and the other 4 sets for training
@author: Chris
"""
#load all proteins and their classification - training
f1 = open("sources/superfamily_level/lff1Comp.txt","r")
lines = f1.readlines()
f1.close()

#load all proteins and their classification - test
f3 = open("sources/superfamily_level/lff1.txt","r")
lines2 = f3.readlines()
f3.close()
#training
training = list()
#test
test = list()

#name and fold
#create lists with both
for x in lines:
    y = x.split()[0]
    name = y[1:len(y)]
    z = x.split()[1]
    class_only = z.split('.')[0]
    fold_only = z.split('.')[1]    
    superfamily_only = z.split('.')[2]
    superfamily = class_only+"."+fold_only+"."+superfamily_only
    pair = list()
    pair.append(name)
    pair.append(superfamily)
    training.append(pair)

for x in lines2:
    y = x.split()[0]
    name = y[1:len(y)]
    z = x.split()[1]
    class_only = z.split('.')[0]
    fold_only = z.split('.')[1]    
    superfamily_only = z.split('.')[2]
    superfamily = class_only+"."+fold_only+"."+superfamily_only
    pair = list()
    pair.append(name)
    pair.append(superfamily)
    test.append(pair)

print "Training: %d -- Test: %d"%(len(training) , len(test))
print "total: %d"%(len(training)+len(test))
    
#header of the training file
f2 = file("sources/superfamily_level/trainingDataset.arff","w")
f2.write("%1. Title: Normalized Profiles\n")
f2.write("%2. Sources:\n")
f2.write("%\t\t(a) Creator: Christian Charry\n")
f2.write("%\t\t(b) Date: May 2017\n")
f2.write("@RELATION NP\n")
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
f2.write("@ATTRIBUTE class {d.144.1,b.18.1,b.1.18,c.23.1,c.3.1,a.4.1,a.4.5,b.1.2,b.1.1,d.17.4,c.66.1,d.58.7,c.47.1,c.55.1,a.1.1,b.55.1,a.45.1,b.47.1,c.94.1,d.15.1,b.36.1,c.67.1,d.108.1,c.69.1,g.37.1,a.39.1,g.39.1,c.108.1,c.55.3,b.40.4,b.34.2,c.93.1,d.38.1,c.2.1,c.37.1,a.25.1,c.1.9,c.1.8,b.29.1,c.14.1,b.82.1,c.1.10}\n")
f2.write("@DATA\n")

#now for the 80% of proteins we create the training row
thisName = ""
thisClass = ""

for i in training:
    thisName = i[0]
    thisClass = i[1]     
    f = open("normalized/normalized-profile-(%s).txt"%thisName,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f2.write("%s, %s\n"%(formattedProfile,thisClass))

f2.close()    
#header of the training file
f3 = file("sources/superfamily_level/testDatasetRandom.arff","w")
f3.write("%1. Title: Normalized Profiles\n")
f3.write("%2. Sources:\n")
f3.write("%\t\t(a) Creator: Christian Charry\n")
f3.write("%\t\t(b) Date: May 2017\n")
f3.write("@RELATION NP\n")
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
f3.write("@ATTRIBUTE class {d.144.1,b.18.1,b.1.18,c.23.1,c.3.1,a.4.1,a.4.5,b.1.2,b.1.1,d.17.4,c.66.1,d.58.7,c.47.1,c.55.1,a.1.1,b.55.1,a.45.1,b.47.1,c.94.1,d.15.1,b.36.1,c.67.1,d.108.1,c.69.1,g.37.1,a.39.1,g.39.1,c.108.1,c.55.3,b.40.4,b.34.2,c.93.1,d.38.1,c.2.1,c.37.1,a.25.1,c.1.9,c.1.8,b.29.1,c.14.1,b.82.1,c.1.10}\n")
f3.write("@DATA\n")

#now for the 20% of proteins we create the testing row
thisName = ""
thisClass = ""

for i in test:
    thisName = i[0]
    thisClass = i[1]       
    f = open("normalized/normalized-profile-(%s).txt"%thisName,'r')#open the normalized protein file for the data
    data = f.readline()
    f.close()
    vector = data.split()
    separator = ", "
    formattedProfile = separator.join(vector)#format the lff profile of the protein
    f3.write("%s, %s\n"%(formattedProfile,thisClass))

f3.close()    

