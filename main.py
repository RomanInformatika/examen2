f=open('students.csv',encoding='UTF8').read()
f=f.split('\n')
a=[]
for i in f:
    a.append(i.split(','))
print(a)
for el in a:
    if 'Хадаров Владимир' in el[1]:
        print('Ты получил: '+ el[4]+ ', за проект-'+el[2])

summ=0
cnt=0
for el in a:
    if el[4]!='None':
        summ+=int(el[4])
        cnt+=1
avg=round(summ/cnt,3)

for el in a:
    if el[4]=='None':
        el[4]=str(avg)

f=open("student_new.csv","w")
for el in a:
    f.write(','.join(el)+'\n')
#########################################################################

for i in range(1,len(a)):
    x=a[i]
    j=i
    while j>0 and float(a[j - 1][4]) > float(x[4]):
        a[j] = a[j - 1]
        j-=1
    a[j]=x


b=[]
for el in a:
    if '10' in el[3] and el[4]=='5':
        b.append(el)



for i in range(3):

    shortName=getShortName(b[i][1])
    print(str(i+1)+' место: '+shortName)
