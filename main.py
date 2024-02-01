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