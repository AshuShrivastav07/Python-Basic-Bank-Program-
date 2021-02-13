import datetime
def add(a,b):
    t=(a+b)
    return(t)
def lose(a,b):
    t=(a-b)
    return(t)
#Progaram Start From Here....
f=open("ac data.py","a")
print("Welcome to World of Bank :- ")
print("\n")
for i in range(999):
    print("\n")
    Ac_Hn=input("Enter Name :- ")
    c=(Ac_Hn.isalnum())     
    if(c==True):   
         print("Please Enter Account Holder Name again...") 
         continue
    f.writelines("Account Holder Name :- ")
    f.writelines((Ac_Hn).capitalize())
    print("\n")
    Ac_no=input("Enter Your A/c No :- ")
    sum=0
    f.writelines("\n")
    f.writelines("Account No. ")
    f.writelines(str(Ac_no))
    f.writelines("\n")
    x=datetime.datetime.today()
    f.writelines("Date of Transaction :- ")
    f.writelines(str(x))
    ab=500
    f.writelines("\n")
    f.writelines("Your Total Balance :- ")
    print("\n")
    print("What Do You Want To Do ?")
    print("\n")
    for i in range(0,2):
        s1=print("1 for Diposit ")
        print("\n")
        s2=print("2 For withdrawal ")
        print("\n")
        ch=input()
        print("\n")
        if(ch=="1"):
            a=int(input("Enter Amount to Diposite :- "))
            print("\n")
            if(a<10000):    
                t1=add(a,ab)
                print("Your Total Balance :- ", t1)
                print("\n")
                f.writelines(str(t1)) 
                f.writelines("\n")
                f.writelines("________________________________________")
                f.writelines("\n")

                print("\n")
                break
            elif("a">="10001"):
                print("Please enter Amount Again")
                print("\n")
                continue    
        elif(ch=="2"):
            ac=int(input("Enter Amount to Withdrawal : - "))
            if(ac<ab):
                t2=lose(ab,ac)
                print("\n")
                print("Your Total Balance :- ",t2)
                f.writelines(str(t2))
                f.writelines("\n")
                f.writelines("________________________________________")
                f.writelines("\n")
                print("\n")
                break
            elif(ac>ab):
                print("insufficient balance")
                print("\n")
                continue
                print("\n")
        
    c=input("Enter y For Again and n for cancel :- ")
    if(c=="y"):
        continue
    elif(c=="n"): 
        break
