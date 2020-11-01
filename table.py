import os 
print("\033[32m")
os.system("toilet -f mono12 -F border Table")
print()
while True:
    Num = int(input("\033[31m""Enter The Table Number :- "))
    for i in range(1,11):
        n = Num*i
        print("\033[33m",Num,'x',i,'=',n)
