

#Într-un fişier sunt înscrise caractere arbitrare. Elaboraţi un program
#care afişează pe ecran numărul vocalelor din fişier.

f=open('D:/Text.txt','w')
a=str(input('dati caracterele:'))
f.write(a)

f=open('D:/Text.txt','r')
y=f.read()
print(y)
x=[]

for i in range (0,len(y)):
    if y[i]=='a' or y[i]=='A' or y[i]=='e' or y[i]=='E' or y[i]=='i' or y[i]=='I' or y[i]=='o' or y[i]=='O' or y[i]=='u' or y[i]=='U':
        x.extend(y[i])

y=str(len(x))
f=open('D:/Vocale.txt','w')
f.write(str(x))
f.write('\n')
f.write('numarul de vocale din sir: ')
f.write(y)
f.close()

f=open("D:/Vocale.txt","r")
b=f.read()
print("Vocalele din sir sunt:", b)
f.close()