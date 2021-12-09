f=open('C:/Users/Staie-10-C100/Desktop/listdavid.txt','rt')
print('Numar Nota 1 Nota 2 Nota 3')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
l=list(f)
with open('C:/Users/Staie-10-C100/Desktop/fisierreserva.txt','w') as a:
    for i in l:
        print()

for j in l:
    m=j.split()
    sn=((float(j[2])+float(j[3])+float(j[4])))
    media=(sn/3)
    print(media)
    b=open('medii.txt','b')
    