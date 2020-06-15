def Num1(n):
    choice1=0
    for i in range(3):
        a=random.randint(1,6)
        choice1=choice1+a
    beishu=0
    if n==choice1:
        print ("恭喜压中啦")
        beishu=10
    elif ((n in range(3,11)) and (choice1 in range(3,11))) or ((n in range(11,19)) and (choice1 in range(11,19))):
        print ("压中大小")
        beishu=2
    else:
        print ("未压中")
    return beishu
allmoney=100
def choice2(money,yourchoice):
    global allmoney
    allmoney=allmoney-money
    status=Num1(yourchoice)
    print (status)
    allmoney=allmoney+status*money
    return allmoney
'''
print ("还剩{0}".format(choice2(10,5)))
print (allmoney)
print ("还剩{0}".format(choice2(10,5)))
print (allmoney)
'''
status='true'
while status=='true':
    money=int(input("请输入押注金额："))
    choice=int(input("请输入押注选择："))
    if allmoney<money:
        print ("余额不足")
    else
    print("还剩{0}".format(choice2(money,choice)))
    if allmoney==0:
        status='false'
