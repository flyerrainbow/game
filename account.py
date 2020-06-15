
import csv
import datetime

def keepAccounts():
    f=open('1.csv','a',encoding='utf-8',newline=''"")
    keeptime=datetime.date.today()
    mingmu=input("名目:")
    money=int(input("金额:"))
    csv_writer=csv.writer(f)
    csv_writer.writerow([keeptime,mingmu,money])
    f.close()
def checkAccount():
    f = open('1.csv', 'r',encoding='utf-8')
    csv_reader=csv.reader(f)
    sum1=0
    for i in csv_reader:
        #print (i[2])
        #print (type(i[2]))
        sum1=sum1+int(i[2])
    print (sum1)
def printAccount():
    f = open('1.csv', 'r', encoding='utf-8')
    csv_reader = csv.reader(f)
    for i in csv_reader:
        print (','.join(i))
while True:
    a = input("选择操作：\n1.记账\n2.查余额\n3.收支明细\n")
    if a=='1':
        keepAccounts()
    elif a=='2':
        checkAccount()
    elif a=='3':
        printAccount()
    else:
        print ('退出记账本')
        break


