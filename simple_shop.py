n=1  #for whileloop
#list of items
items=["1.rice\n","2.sugar\n", "3.wheat\n", "4.maida\n","5.pen\n","6.pencil\n","7.book\n","8.bread\n","9.biscuit\n","10.eraser\n"]
stationary=["pen","book","pencil"]
grocery=["rice","egg","milk"]
#cart array and catogary   
cat=["1.All items","2.stationary","3.grocery"]
cart=[]
print("******************")
print("*Project shopping*")
print("******************")

admin="dhruva"
#---------------shoping site funtion-------------------------------
def shop_site():
        print("***************************\nwelcome " +admin +"\n***************************")
        print("Today's shopping Avialable items")
        global n
       # m=3
    #*****************************Code begins if login is true****************************
           
        #----------------catogary choice----------------------------  
        print("Choose the catagory\n")
        for i in cat:
            print(i)
        cat_cho=int(input())
        #--------------All items-----------------
        if cat_cho == 1:
            for i in items:
                print(i)
            while n<3:
                a = int(input("select your item : "))
                print("added successfully to the cart")
                
                
                
                cart.append(items[a-1]) 
                cont=int(input("Do you want to contiue shopping? in All items\npress 1:yes\n2:no\n "))
                if cont == 1:
                    continue
                elif cont ==2:
                    n=4
                #elif cont ==3:
                 #code for going back to category  yet to write 
                else:
                    print("Invalid choice")
        #---------------------choice stationary--------------
        elif cat_cho == 2:
            for i in stationary:
                print(i)
            while n<3:
                a = int(input("select your item : "))
                print("added successfully to the cart")
                
                
                cart.append(stationary[a-1])
                
                cont=int(input("Do you want to contiue shopping? in \npress 1:yes\n2:no\n"))
                if cont == 1:
                    continue
                elif cont ==2:
                    n=4
                else:
                    print("Invalid choice")
        #------------------choice grocery----------------------
        elif cat_cho == 3:
            for i in grocery:
                print(i)
            while n<3:
                a = int(input("select your item : "))
                print("added successfully to the cart")
                
                
                cart.append(grocery[a-1])
                
                cont=int(input("Do you want to contiue shopping? in \npress 1:yes\n2:no\n"))
                if cont == 1:
                    continue
                elif cont ==2:
                    n=4
                else:
                    print("Invalid choice")            
        print("your cart is: ")
        print("-------------------------------------")
        print("Item List")
        print("-------------------------------------")
        
        for i in cart:
            print(i)       
        print("-------------------------------------")

#********************user login function*******************************
def login_check():
    signin=int(input(("Enter 1 to login \n Enter 2 to Exit\n")))
    if signin == 1:
        name=input("enter your username: \n")
        passco=input("enter your password\n")
        if passco=="pass" and name=="boss":
            shop_site()
        else :
            print("Invlaid username or password")
            login_check()
    
    elif signin ==2: exit()

login_check()

    