import re
import os
import random
class password:
    def __init__(self,pas):
        self.pas=pas
    def message(self):
        print("The password is Acceptable.\n")
        p=input("\nEnter the password : ")
        l1=[1,2,3,4,5,6,7,8,9,0]
        l2=["+","-","X"]
        if(p==self.pas):
            print("\nCAPTCHA : ")
            a=random.choice(l1)
            b=random.choice(l2)
            c=random.choice(l1)
            print(a," ",b," ",c," = ",end=" ")
            n=int(input())
            if(b=="+"):
                if(n==a+c):
                    print("Hi programmer..! Your Code is verified..!!\n")
                else:
                    print("WRONG CAPTCHA !!\n")
            if(b=="-"):
                if(n==a-c):
                    print("Hi programmer..! Your Code is verified..!!\n")
                else:
                    print("WRONG CAPTCHA !!\n")
            if(b=="X"):
                if(n==a*c):
                    print("Hi programmer..! Your Code is verified..!!\n")
                else:
                    print("WRONG CAPTCHA !!\n")
        else:
            print("WRONG PASSWORD !!\n")
print("\n\t\t\t*****PASSWORD GENERATOR*****")
print("\n\n\n\nSet a valid Password with the following instructions : \n")
print("-> It should have atleast 8 characters.")
print("-> It should have atleast one Uppercase letter (Ex : A,B,C....etc).")
print("-> It should have atleast one Lowercase letter (Ex : a,b,c....etc).")
print("-> It should have atleast one Number (Ex : 1,2,3....etc).")
print("-> It should have atleast one special character (Ex : @,!,#,$,&).")
print("\nNOTE : PLEASE GIVE A STRONG PASSWORD.")
txt=input("\n\n\nMake a password : ")
res1=re.search("[a-z]",txt)
res2=re.search("[A-Z]",txt)
res3=re.search("[0-9]",txt)
res4=re.search("[!@#$&]",txt)
x=password(txt)
if (res1 and res2 and res3 and res4 and (len(txt)>=8)):
    os.system("cls")
    x.message()
else:
    print("The password is not Acceptable.")

