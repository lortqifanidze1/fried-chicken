#none-s yuradegba ar miaqciot
def capybara(a):
    print("1 = create account / 2 = Deposit/ 3 = Withdraw / 4 = Exit ")
    
    money = 100 
    if a == 1:
        return input("Name :")
    elif a == 2:
        def gamar(yy):
            
         a= input("Who to Deposit :")
         if money >= int(yy):
            return print(f"you have deposited {a}"), money - yy ,"$"
         else:
             return print("you dont have enoght")
        hh = gamar(int(input()))
        print(hh)
    elif a == 3:
        def la(da):
            
            if money >= int(da):
                return "you withdawed" ,money - da
            else:
                return "not enoght money"
        jaja = la(int(input()))
        print(jaja)
        
    else:
        return "Exit"
# type here what you want 
r = capybara()
print(r)
