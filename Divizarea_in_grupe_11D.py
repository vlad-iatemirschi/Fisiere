with open('D:/Lista clasei 11D.txt','r') as f:

    linii=list(f)
    f.close()

#afisarea si media totala

n=media=0
print('Nume','Prenume','Nota','Grupa',sep='\t')
for linie in linii:
    campuri=linie.split()
    nota=int(campuri[2])
    n,media=n+1,media+nota
    print(linie)    
media1=media2=0
print("Media celor",n,"studenti este",round(media/n,2))

#divizarea si media pe grupe

x1=x2=0
grupa1=[]
grupa2=[]

for linie in linii:
    campuri=linie.split()
    if campuri[3]=="engl1":
        media1+=int(campuri[2])
        x1+=1
        grupa1.extend([linie])
    if campuri[3]=="engl2":
        x2+=1
        media2+=int(campuri[2])
        grupa2.extend([linie]) 

print("Media elevilor din grupa 1 este",round(media1/x1,2))
print("Media elevilor din grupa 2 este",round(media2/x2,2))

#introducerea in fisiere

with open("D:/Grupa1.txt","w") as f:
    for i in grupa1:    
        f.write(i)
        f.write("\n")
with open("D:/Grupa2.txt","w") as f:
    for i in grupa2:    
        f.write(i)
        f.write("\n")