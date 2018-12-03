import random
#load all proteins and their classification
f1 = open("SCOPclassifications.txt","r")
lines = f1.readlines()
f1.close()
f2 = file("lff1.txt","w")
f3 = file("lff2.txt","w")
f4 = file("lff3.txt","w")
f5 = file("lff4.txt","w")
f6 = file("lff5.txt","w")
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
#create lists 
for x in lines:
    y = x.split()[0]
    name = y[1:len(y)]
    z = x.split()[1]
    classification = z[0:1]
    if classification == 'a':
        classA.append(x)
    elif classification == 'b':
        classB.append(x)
    elif classification == 'c':
        classC.append(x)
    elif classification == 'd':
        classD.append(x)
    elif classification == 'e':
        classE.append(x)
    elif classification == 'f':
        classF.append(x)
    elif classification == 'g':
        classG.append(x)
        
print "classA: %d, classB: %d, classC: %d, classD: %d, classE: %d, classF: %d, classG: %d"%(len(classA),len(classB),len(classC),len(classD),len(classE),len(classF),len(classG))
print "total: %d"%(len(classA)+len(classB)+len(classC)+len(classD)+len(classE)+len(classF)+len(classG))

for i in classA:
    for i in range(471):
        idx = random.randint(0,(len(classA)-1))
        protein = classA[idx]#choose a random protein
        f2.write(protein)
        del classA[idx]
        idx = random.randint(0,(len(classA)-1))
        protein = classA[idx]#choose a random protein
        f3.write(protein)
        del classA[idx]
        idx = random.randint(0,(len(classA)-1))
        protein = classA[idx]#choose a random protein
        f4.write(protein)
        del classA[idx]
        idx = random.randint(0,(len(classA)-1))
        protein = classA[idx]#choose a random protein
        f5.write(protein)
        del classA[idx]
        idx = random.randint(0,(len(classA)-1))
        protein = classA[idx]#choose a random protein
        f6.write(protein)
        del classA[idx]
    idx = random.randint(0,(len(classA)-1))
    protein = classA[idx]#choose a random protein
    f6.write(protein)
    del classA[idx]    

for i in classB:
    for i in range(543):
        idx = random.randint(0,(len(classB)-1))
        protein = classB[idx]#choose a random protein
        f2.write(protein)
        del classB[idx]
        idx = random.randint(0,(len(classB)-1))
        protein = classB[idx]#choose a random protein
        f3.write(protein)
        del classB[idx]
        idx = random.randint(0,(len(classB)-1))
        protein = classB[idx]#choose a random protein
        f4.write(protein)
        del classB[idx]
        idx = random.randint(0,(len(classB)-1))
        protein = classB[idx]#choose a random protein
        f5.write(protein)
        del classB[idx]
        idx = random.randint(0,(len(classB)-1))
        protein = classB[idx]#choose a random protein
        f6.write(protein)
        del classB[idx]
    for i in range(2):
        idx = random.randint(0,(len(classB)-1))
        protein = classB[idx]#choose a random protein
        f6.write(protein)
        del classB[idx]   

for i in classC:
    for i in range(763):
        idx = random.randint(0,(len(classC)-1))
        protein = classC[idx]#choose a random protein
        f2.write(protein)
        del classC[idx]
        idx = random.randint(0,(len(classC)-1))
        protein = classC[idx]#choose a random protein
        f3.write(protein)
        del classC[idx]
        idx = random.randint(0,(len(classC)-1))
        protein = classC[idx]#choose a random protein
        f4.write(protein)
        del classC[idx]
        idx = random.randint(0,(len(classC)-1))
        protein = classC[idx]#choose a random protein
        f5.write(protein)
        del classC[idx]
        idx = random.randint(0,(len(classC)-1))
        protein = classC[idx]#choose a random protein
        f6.write(protein)
        del classC[idx]

for i in classD:
    for i in range(649):
        idx = random.randint(0,(len(classD)-1))
        protein = classD[idx]#choose a random protein
        f2.write(protein)
        del classD[idx]
        idx = random.randint(0,(len(classD)-1))
        protein = classD[idx]#choose a random protein
        f3.write(protein)
        del classD[idx]
        idx = random.randint(0,(len(classD)-1))
        protein = classD[idx]#choose a random protein
        f4.write(protein)
        del classD[idx]
        idx = random.randint(0,(len(classD)-1))
        protein = classD[idx]#choose a random protein
        f5.write(protein)
        del classD[idx]
        idx = random.randint(0,(len(classD)-1))
        protein = classD[idx]#choose a random protein
        f6.write(protein)
        del classD[idx]
    for i in range(4):
        idx = random.randint(0,(len(classD)-1))
        protein = classD[idx]#choose a random protein
        f6.write(protein)
        del classD[idx] 

for i in classE:
    for i in range(44):
        idx = random.randint(0,(len(classE)-1))
        protein = classE[idx]#choose a random protein
        f2.write(protein)
        del classE[idx]
        idx = random.randint(0,(len(classE)-1))
        protein = classE[idx]#choose a random protein
        f3.write(protein)
        del classE[idx]
        idx = random.randint(0,(len(classE)-1))
        protein = classE[idx]#choose a random protein
        f4.write(protein)
        del classE[idx]
        idx = random.randint(0,(len(classE)-1))
        protein = classE[idx]#choose a random protein
        f5.write(protein)
        del classE[idx]
        idx = random.randint(0,(len(classE)-1))
        protein = classE[idx]#choose a random protein
        f6.write(protein)
        del classE[idx]
    idx = random.randint(0,(len(classE)-1))
    protein = classE[idx]#choose a random protein
    f6.write(protein)
    del classE[idx] 

for i in classF:
    for i in range(44):
        idx = random.randint(0,(len(classF)-1))
        protein = classF[idx]#choose a random protein
        f2.write(protein)
        del classF[idx]
        idx = random.randint(0,(len(classF)-1))
        protein = classF[idx]#choose a random protein
        f3.write(protein)
        del classF[idx]
        idx = random.randint(0,(len(classF)-1))
        protein = classF[idx]#choose a random protein
        f4.write(protein)
        del classF[idx]
        idx = random.randint(0,(len(classF)-1))
        protein = classF[idx]#choose a random protein
        f5.write(protein)
        del classF[idx]
        idx = random.randint(0,(len(classF)-1))
        protein = classF[idx]#choose a random protein
        f6.write(protein)
        del classF[idx]
    idx = random.randint(0,(len(classF)-1))
    protein = classF[idx]#choose a random protein
    f6.write(protein)
    del classF[idx]

for i in classG:
    for i in range(138):
        idx = random.randint(0,(len(classG)-1))
        protein = classG[idx]#choose a random protein
        f2.write(protein)
        del classG[idx]
        idx = random.randint(0,(len(classG)-1))
        protein = classG[idx]#choose a random protein
        f3.write(protein)
        del classG[idx]
        idx = random.randint(0,(len(classG)-1))
        protein = classG[idx]#choose a random protein
        f4.write(protein)
        del classG[idx]
        idx = random.randint(0,(len(classG)-1))
        protein = classG[idx]#choose a random protein
        f5.write(protein)
        del classG[idx]
        idx = random.randint(0,(len(classG)-1))
        protein = classG[idx]#choose a random protein
        f6.write(protein)
        del classG[idx]
    idx = random.randint(0,(len(classG)-1))
    protein = classG[idx]#choose a random protein
    f6.write(protein)
    del classG[idx]
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
