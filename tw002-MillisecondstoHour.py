print("###  This program converts milliseconds into hours, minutes, and seconds ###\n\n\
(To exit the program, please type 'exit')")


h = 3600000
m = 60000
s = 1000

t = True
while t:
    num = input("\nPlease enter the milliseconds (should be greater than zero) :").strip().lower()
    
    if num.isdigit() and int(num) >= 1:
        num2 = int(num)
        numh = num2 // h
        numm = (num2 % h) // m
        nums = (num2 % m) // s
        
        
        if numh != 0 and numm != 0 and nums != 0:
            print(f"\n{numh} hour/s {numm} minute/s {nums} second/s")
        
        elif numh == 0 and numm != 0 and nums != 0:
            print(f"\n{numm} minute/s {nums} second/s")
            
        elif numh == 0 and numm == 0 and nums != 0:
            print(f"\n{nums} second/s")
            
        elif numh != 0 and numm == 0 and nums != 0:
            print(f"\n{numh} hour/s {nums} second/s")
            
        elif numh == 0 and numm == 0 and nums== 0:            
            print(f"\njust {num2} millisecond/s")
           
        elif numh == 0 and numm != 0 and nums== 0:            
            print(f"\n{numm} minute/s")
            
        elif numh != 0 and numm == 0 and nums== 0:            
            print(f"\n{numh} hour/s")     
        
        elif numh != 0 and numm != 0 and nums== 0:            
            print(f"\n{numh} hour/s {numm} minute/s")
        
    elif num == "exit":
        print("\nExiting the program... Good Bye")
        t = False
        
    else:
        print("\nNot Valid Input !!!")