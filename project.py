import mysql.connector as sqltor
from prettytable import PrettyTable
from datetime import date
db=sqltor.connect(host="localhost" , user="root" , passwd="B#@w@+123" , database="chaatshop")
curr=db.cursor()
def add():
    print("============================================================")
    token_no=int(input("Enter the token no of the new food item : "))
    name=input("Enter the name of the food item available : ")
    price=int(input("Enter the price of the food item : "))
    query="insert into chaat values('%s','%s','%s')"%(token_no,name,price)
    curr.execute(query)
    db.commit()
    print("New Food Item added in Menu")
    print("============================================================")
def rate_change():
    print("============================================================")
    token_no=int(input("Enter the token no of the food item whose price is to be changed : "))
    price=int(input("Enter the new price of the food item : "))
    query="update chaat set price='%s' where token_no='%s'"%(price,token_no)
    curr.execute(query)
    db.commit()
    print("Food Item Menu Updated")
    print("============================================================")
def delete():
    print("============================================================")
    token_no=int(input("Enter the token no of the food item which has to be deleted : "))
    query="delete from chaat where token_no='%s'"%(token_no)
    curr.execute(query)
    db.commit()
    print("Food Item with token no",token_no,"has been successfully deleted")
    print("============================================================")
def display():
    print("============================================================")
    query="select * from chaat"
    curr.execute(query)
    f=curr.fetchall()
    myTable = PrettyTable(["token_no","name_of_fooditem","price_in_rupees"])
    for i in f:
        myTable.add_row(list(i))
    print(myTable)
    print("")
    print("============================================================")
def search():
    print("============================================================")
    token_no=int(input("Enter the token no of the food item you want to search : "))
    query="select * from chaat where token_no='%s'"%(token_no)
    curr.execute(query)
    g=curr.fetchall()
    for i in g:
        myTable = PrettyTable(["token_no","name_of_chaat","price_in_rupees"])
        myTable.add_row(list(i))
        print(myTable)
    print("============================================================")
def shopping():
    print("============================================================")
    print("MENU CARD")
    display()
    token_no=int(input("Enter the token no of the food item you want to buy : "))
    query="select * from chaat where token_no='%s'"%(token_no)
    curr.execute(query)
    g=curr.fetchall()
    for i in g:
        myTable = PrettyTable(["token_no","name_of_chaat","price_in_rupees"])
        myTable.add_row(list(i))
        print(myTable)
    db.commit()
    res=input("are you sure that you want to buy this food item? (y/n) : ")
    if res.lower()=="y":
        on=0
        print("Customer Details Please")
        name=input("Enter your name : ")
        email=input("Enter your email id : ")
        contact_no=int(input("Enter your contact no : "))
        print("")
        print("Order details : ")
        qty=int(input("Enter the quantity you would like to have : "))
        if qty==0:
            print("Sorry 0 items can't be ordered...")
            print("Better if you put order confirmation to no <choice 'n'> ")
            shopping()
        query="select price from chaat where token_no='%s'"%(token_no)
        curr.execute(query)
        pricee=curr.fetchall()
        for i in pricee:
            j = ''.join(str(x) for x in i)
            totprice=int(j)*qty
        print("Total amount to be paid : ",totprice)
        print("Order has been placed successfully")
        print("Invoice successfully generated")
        print("Thank You for shopping with YumYum Snacks house")
        date1=date.today()
        #date=today.strftime("%d %m %Y")
        on+=1
        invl=[]
        invl.append("YumYum Snacks House".center(120)+"\n")
        invl.append("Naagu Shopping Complex, Shop No. 420, AngryLand".center(120)+'\n')
        invl.append(""+'\n')
        invl.append("Order Date : ")
        invl.append(str(date1)+"\n")
        invl.append("Order Number : ")
        invl.append(str(on))
        invl.append(""+'\n')
        invl.append(""+'\n')
        invl.append("Customer Details".center(120)+'\n')
        invl.append("Name : ")
        invl.append(name+'\n')
        invl.append("Email : ")
        invl.append(email+'\n')
        invl.append("Phone Number : ")
        invl.append(str(contact_no)+'\n')
        invl.append("Order Details".center(120)+'\n')
        invl.append("Food Item Choice : ")
        query="select name_of_chaat from chaat where token_no='%s'"%(token_no)
        curr.execute(query)
        pricee=curr.fetchall()
        for i in pricee:
            j = ''.join(str(x) for x in i)
        db.commit()
        invl.append(j+'\n')
        invl.append("Quantity Of the Food Item Ordered : ")
        invl.append(str(qty)+'\n')
        invl.append(""+'\n')
        invl.append(""+'\n')
        invl.append("Total Amount Paid : ")
        invl.append(totprice)
        with open(r"C:\Users\Nimesh\Desktop\mcs\invoice_"+str(qty)+"_"+name+"_"+str(on)+".txt","w+") as f:
            for items in invl:
                f.write('%s\n' %items)
        print("============================================================")
    if res.lower()=="n":
        print("Order Successfully Cancelled...")
        print("Thank You for visiting YumYum Snacks house")
        print("============================================================")
while True:
    print("============================================================".center(120))
    print("WELCOME TO YUMYUM SNACKS HOUSE !!".center(120))
    print("THE ONLY PLACE AMONG ALL THE SHOPS ON ANGRYLAND".center(120))
    print("WHERE HYGIENE AND HEALTHY FOOD ARE OUR FIRST PRIORITY".center(120))
    print("ALL RIGHTS GRANTED, MENU CARD RIGHTS ALSO GRANTED :) ")
    print("So What Would You Like to do Today ?? ")
    print("1. Add a New Food Item")
    print("2. Change the Rate of Existing Food Item")
    print("3. Delete a Food Item")
    print("4. Display the Menu Card")
    print("5. Search for a Food Item")
    print("6. Place An Order")
    print("7. Exit")
    ch=int(input("Enter your choice : "))
    if ch==1:
        add()
    elif ch==2:
        rate_change()
    elif ch==3:
        delete()
    elif ch==4:
        display()
    elif ch==5:
        search()
    elif ch==6:
        shopping()
    elif ch==7:
        exit()
    else:
        print("Try again...")
