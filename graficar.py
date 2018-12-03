
s=""
for i in range(1,101,1):
    f = open('clustering/10MEDOIDS2-%i.txt'%i,'r')    
    lines = f.readlines()
    f.close()
    contador=1
    for x in lines:
        y=x.split()
        
        for d in y:
            s=s+"%s\t"%d            
            if contador%10==0:
                s=s+"\n"
            contador=contador+1
            
    s=s+"\n\n\n"            
s=s.replace(".",",")
print(s)
