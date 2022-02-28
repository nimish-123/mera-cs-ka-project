print("Welcome to YumYum Chaat Centre".center(120))
print("Where Hygiene and Customer Satisfaction is our Priority".center(120))

import mysql.connector
sql_connector=mysql.connector.connect(host="localhost",user="root",passwd="B#@w@+123",database="tikku")
sql_cursor=sql_connector.cursor()


def edit():
    print("")
    print("What Amendments You Want To Make??")
    print("1. Change Of Rate")
    print("2. Add A Food Item")
    print("3. Delete A Food Item")
    task=int(input("Enter Choice --> "))
    if task==1:
        sql_cursor.execute("use tikku")
        sql_cursor.execute("select * from yummy")
        data=sql_cursor.fetchall()
        a=(data[0])[1]
        b=(data[1])[1]
        c=(data[2])[1]
        d=(data[3])[1]
        e=(data[4])[1]
        f=(data[5])[1]
        g=(data[6])[1]
        h=(data[7])[1]
        i=(data[8])[1]
        j=(data[9])[1]
        k=(data[10])[1]
        l=(data[11])[1]
        m=(data[12])[1]
        n=(data[13])[1]
        o=(data[14])[1]
        p=(data[15])[1]
        q=(data[16])[1]
        r=(data[17])[1]
        s=(data[18])[1]
        t=(data[19])[1]
        u=(data[20])[1]
        v=(data[21])[1]
        w=(data[22])[1]
        x=(data[23])[1]
        print("")
        print("")
        print("Chaats Available: ",end="\n")
        if a>0:
            print((data[0])[0],"| ",end="\n")
        if b>0:
            print((data[1])[0],"| ",end="\n")
        if c>0:
            print((data[2])[0],"| ",end="\n")
        if d>0:
            print((data[3])[0],"| ",end="\n")
        if e>0:
            print((data[4])[0],"| ",end="\n")
        if f>0:
            print((data[5])[0],"| ",end="\n")
        if g>0:
            print((data[6])[0],"| ",end="\n")
        if h>0:
            print((data[7])[0],"| ",end="\n")
        if i>0:
            print((data[8])[0],"| ",end="\n")
        if j>0:
            print((data[9])[0],"| ",end="\n")
        if k>0:
            print((data[10])[0],"| ",end="\n")
        if l>0:
            print((data[11])[0],"| ",end="\n")
        if m>0:
            print((data[12])[0],"| ",end="\n")
        if n>0:
            print((data[13])[0],"| ",end="\n")
        if o>0:
            print((data[14])[0],"| ",end="\n")
        if p>0:
            print((data[15])[0],"| ",end="\n")
        if q>0:
            print((data[16])[0],"| ",end="\n")
        if r>0:
            print((data[17])[0],"| ",end="\n")
        if s>0:
            print((data[18])[0],"| ",end="\n")
        if t>0:
            print((data[19])[0],"| ",end="\n")
        if u>0:
            print((data[20])[0],"| ",end="\n")
        if v>0:
            print((data[21])[0],"| ",end="\n")
        if w>0:
            print((data[22])[0],"| ",end="\n")
        if x>0:
            print((data[23])[0],"| ")
        sql_cursor.execute("select Price_In_Rupees from yummy")
        chaat_all=sql_cursor.fetchall()
        while True:
            print("")
            chatrqd=str(input("Enter The Name Of Chaat Whose Rate You Want To Change : "))
            chatrqd=chatrqd.lower()
            if chatrqd=="paani puri":
                chatrqd="Paani Puri"
                ochaat=(chaat_all[0])[0]
                availabl=a
                break
            if chatrqd=="paani puri family pack":
                chatrqd="Paani Puri Family Pack"
                ochaat=(chaat_all[1])[0]
                availabl=b
                break
            if chatrqd=="dahi puri":
                chatrqd="Dahi Puri"
                ochaat=(chaat_all[2])[0]
                availabl=c
                break
            if chatrqd=="american corn dahi puri":
                chatrqd="American Corn Dahi Puri"
                ochaat=(chaat_all[3])[0]
                availabl=d
                break
            if chatrqd=="sev puri":
                chatrqd="Sev Puri"
                ochaat=(chaat_all[4])[0]
                availabl=e
                break
            if chatrqd=="ragda puri":
                chatrqd="Ragda Puri"
                ochaat=(chaat_all[5])[0]
                availabl=f
                break
            if chatrqd=="masala puri":
                chatrqd="Masala Puri"
                ochaat=(chaat_all[6])[0]
                availabl=g
                break
            if chatrqd=="paneer tikki chaat":
                chatrqd="Paneer Tikki Chaat"
                ochaat=(chaat_all[7])[0]
                availabl=h
                break
            if chatrqd=="aaloo tikki chaat":
                chatrqd="Aaloo Tikki Chaat"
                ochaat=(chaat_all[8])[0]
                availabl=i
                break
            if chatrqd=="aaloo tikki chhole":
                chatrqd="Aaloo Tikki Chhole"
                ochaat=(chaat_all[9])[0]
                availabl=j
                break
            if chatrqd=="aaloo chaat":
                chatrqd="Aaloo Chaat"
                ochaat=(chaat_all[10])[0]
                availabl=k
                break
            if chatrqd=="banarasi tamaatar chaat":
                chatrqd="Banarasi Tamaatar Chaat"
                ochaat=(chaat_all[11])[0]
                availabl=l
                break
            if chatrqd=="navratan paapadi chaat":
                chatrqd="Navratan Paapadi Chaat"
                ochaat=(chaat_all[12])[0]
                availabl=m
                break
            if chatrqd=="paalak patta chaat":
                chatrqd="Paalak Patta Chaat"
                ochaat=(chaat_all[13])[0]
                availabl=n
                break
            if chatrqd=="basket chaat":
                chatrqd="Basket Chaat"
                ochaat=(chaat_all[14])[0]
                availabl=o
                break
            if chatrqd=="katori chaat":
                chatrqd="Katori Chaat"
                ochaat=(chaat_all[15])[0]
                availabl=p
                break
            if chatrqd=="raaj kachori":
                chatrqd="Raaj Kachori"
                ochaat=(chaat_all[16])[0]
                availabl=q
                break
            if chatrqd=="khastaa kachori":
                chatrqd="Khastaa Kachori"
                ochaat=(chaat_all[17])[0]
                availabl=r
                break
            if chatrqd=="khastaa kachori chaat/chhole":
                chatrqd="Khastaa Kachori Chaat/Chhole"
                ochaat=(chaat_all[18])[0]
                availabl=s
                break
            if chatrqd=="samosa":
                chatrqd="Samosa"
                ochaat=(chaat_all[19])[0]
                availabl=t
                break
            if chatrqd=="samosa chaat/chhole":
                chatrqd="Samosa Chaat/Chhole"
                ochaat=(chaat_all[20])[0]
                availabl=u
                break
            if chatrqd=="paapad chhole":
                chatrqd="Paapad Chhole"
                ochaat=(chaat_all[21])[0]
                availabl=v
                break
            if chatrqd=="dahi wadaa":
                chatrqd="Dahi Wadaa"
                ochaat=(chaat_all[22])[0]
                availabl=w
                break
            if chatrqd=="special gulaab jaamun 2 pcs":
                chatrqd="Special Gulaab Jaamun 2 Pcs"
                ochaat=(chaat_all[23])[0]
                availabl=x
                break
            else:
                print("")
                print("..Enter a Valid Choice..".center(120))
        print("")
        print("Earlier the price of", chatrqd ,"counted a single plate was : ", ochaat)
        print("")
        new_price=int(input("New price For the Chaat at your shop is : "))
        sql_cursor.execute("use tikku")
        sql_cursor.execute(("update yummy set Price_In_Rupees = '%s' where Name_Of_Chaat = '%s' ")%(new_price,chatrqd))
        sql_connector.commit()
        print("")
        print("..Amendment Has Been Made..".center(120))
        print("..Check Your Server Or Display Here..(Presss 5)..".center(120))
    elif task==2:
        new_chaat=input("Enter a New Chaat Supply in your shop : ")
        exp_price=input("Enter expected price for sale of the chaat : ")
        sql_cursor.execute("use tikku")
        sql_cursor.execute(("insert into yummy values('%s','%s')")%(new_chaat,exp_price))
        sql_connector.commit()
        print("")
        print("..Amendment Has Been Made..".center(120))
        print("..Check Your Server Or Display Here..(Press 5)..".center(120))
    elif task==3:
        del_chaat=input("Enter the Name of the Food Item You Want To Delete : ")
        sql_cursor.execute("use tikku")
        sql_cursor.execute(("delete from yummy where Name_Of_Chaat = '%s'")%(del_chaat))
        sql_connector.commit()
        print("")
        print("..Searched Food item has been Deleted..".center(120))
        print("..Check Your Server Or Display Here..(Press 5)..".center(120))


def main():
    inv1=open(r"C:\Users\ADMIN\Desktop\Apna Folder\Apna Text 1.log","r")
    inv2=inv1.readlines()
    inv1.close()
    if len(inv2)==0:
        inv1=open(r"C:\Users\ADMIN\Desktop\Apna Folder\Apna Text 1.log","w")
        inv1.write("1000")
        inv1.close()
    inv1=open(r"C:\Users\ADMIN\Desktop\Apna Folder\Apna Text 2.txt","r")
    inv2=inv1.readlines()
    inv3=(inv2[0:0:])
    inv1.close()
    while True:
        sql_cursor.execute("use tikku")
        sql_cursor.execute("select * from yummy")
        data=sql_cursor.fetchall()
        a=(data[0])[1]
        b=(data[1])[1]
        c=(data[2])[1]
        d=(data[3])[1]
        e=(data[4])[1]
        f=(data[5])[1]
        g=(data[6])[1]
        h=(data[7])[1]
        i=(data[8])[1]
        j=(data[9])[1]
        k=(data[10])[1]
        l=(data[11])[1]
        m=(data[12])[1]
        n=(data[13])[1]
        o=(data[14])[1]
        p=(data[15])[1]
        q=(data[16])[1]
        r=(data[17])[1]
        s=(data[18])[1]
        t=(data[19])[1]
        u=(data[20])[1]
        v=(data[21])[1]
        w=(data[22])[1]
        x=(data[23])[1]
        print("")
        print("")
        print("Chaats Available: ",end="\n")
        if a>0:
            print((data[0])[0],"| ",end="\n")
        if b>0:
            print((data[1])[0],"| ",end="\n")
        if c>0:
            print((data[2])[0],"| ",end="\n")
        if d>0:
            print((data[3])[0],"| ",end="\n")
        if e>0:
            print((data[4])[0],"| ",end="\n")
        if f>0:
            print((data[5])[0],"| ",end="\n")
        if g>0:
            print((data[6])[0],"| ",end="\n")
        if h>0:
            print((data[7])[0],"| ",end="\n")
        if i>0:
            print((data[8])[0],"| ",end="\n")
        if j>0:
            print((data[9])[0],"| ",end="\n")
        if k>0:
            print((data[10])[0],"| ",end="\n")
        if l>0:
            print((data[11])[0],"| ",end="\n")
        if m>0:
            print((data[12])[0],"| ",end="\n")
        if n>0:
            print((data[13])[0],"| ",end="\n")
        if o>0:
            print((data[14])[0],"| ",end="\n")
        if p>0:
            print((data[15])[0],"| ",end="\n")
        if q>0:
            print((data[16])[0],"| ",end="\n")
        if r>0:
            print((data[17])[0],"| ",end="\n")
        if s>0:
            print((data[18])[0],"| ",end="\n")
        if t>0:
            print((data[19])[0],"| ",end="\n")
        if u>0:
            print((data[20])[0],"| ",end="\n")
        if v>0:
            print((data[21])[0],"| ",end="\n")
        if w>0:
            print((data[22])[0],"| ",end="\n")
        if x>0:
            print((data[23])[0],"| ")
        sql_cursor.execute("select Price_In_Rupees from yummy")
        price_all=sql_cursor.fetchall()
        while True:
            chaatrqd=str(input("Enter The Name Of Chaat You Want To Have : "))
            chaatrqd=chaatrqd.lower()
            if chaatrqd=="paani puri":
                chaatrqd="Paani Puri"
                price=(price_all[0])[0]
                available=a
                break
            if chaatrqd=="paani puri family pack":
                chaatrqd="Paani Puri Family Pack"
                price=(price_all[1])[0]
                available=b
                break
            if chaatrqd=="dahi puri":
                chaatrqd="Dahi Puri"
                price=(price_all[2])[0]
                available=c
                break
            if chaatrqd=="american corn dahi puri":
                chaatrqd="American Corn Dahi Puri"
                price=(price_all[3])[0]
                available=d
                break
            if chaatrqd=="sev puri":
                chaatrqd="Sev Puri"
                price=(price_all[4])[0]
                available=e
                break
            if chaatrqd=="ragda puri":
                chaatrqd="Ragda Puri"
                price=(price_all[5])[0]
                available=f
                break
            if chaatrqd=="masala puri":
                chaatrqd="Masala Puri"
                price=(price_all[6])[0]
                available=g
                break
            if chaatrqd=="paneer tikki chaat":
                chaatrqd="Paneer Tikki Chaat"
                price=(price_all[7])[0]
                available=h
                break
            if chaatrqd=="aaloo tikki chaat":
                chaatrqd="Aaloo Tikki Chaat"
                price=(price_all[8])[0]
                available=i
                break
            if chaatrqd=="aaloo tikki chhole":
                chaatrqd="Aaloo Tikki Chhole"
                price=(price_all[9])[0]
                available=j
                break
            if chaatrqd=="aaloo chaat":
                chaatrqd="Aaloo Chaat"
                price=(price_all[10])[0]
                available=k
                break
            if chaatrqd=="banarasi tamaatar chaat":
                chaatrqd="Banarasi Tamaatar Chaat"
                price=(price_all[11])[0]
                available=l
                break
            if chaatrqd=="navratan paapadi chaat":
                chaatrqd="Navratan Paapadi Chaat"
                price=(price_all[12])[0]
                available=m
                break
            if chaatrqd=="paalak patta chaat":
                chaatrqd="Paalak Patta Chaat"
                price=(price_all[13])[0]
                available=n
                break
            if chaatrqd=="basket chaat":
                chaatrqd="Basket Chaat"
                price=(price_all[14])[0]
                available=o
                break
            if chaatrqd=="katori chaat":
                chaatrqd="Katori Chaat"
                price=(price_all[15])[0]
                available=p
                break
            if chaatrqd=="raaj kachori":
                chaatrqd="Raaj Kachori"
                price=(price_all[16])[0]
                available=q
                break
            if chaatrqd=="khastaa kachori":
                chaatrqd="Khastaa Kachori"
                price=(price_all[17])[0]
                available=r
                break
            if chaatrqd=="khastaa kachori chaat/chhole":
                chaatrqd="Khastaa Kachori Chaat/Chhole"
                price=(price_all[18])[0]
                available=s
                break
            if chaatrqd=="samosa":
                chaatrqd="Samosa"
                price=(price_all[19])[0]
                available=t
                break
            if chaatrqd=="samosa chaat/chhole":
                chaatrqd="Samosa Chaat/Chhole"
                price=(price_all[20])[0]
                available=u
                break
            if chaatrqd=="paapad chhole":
                chaatrqd="Paapad Chhole"
                price=(price_all[21])[0]
                available=v
                break
            if chaatrqd=="dahi wadaa":
                chaatrqd="Dahi Wadaa"
                price=(price_all[22])[0]
                available=w
                break
            if chaatrqd=="special gulaab jaamun 2 pcs":
                chaatrqd="Special Gulaab Jaamun 2 Pcs"
                price=(price_all[23])[0]
                available=x
                break
            else:
                print("")
                print("..Enter a Valid Choice..".center(120))
        print("")
        print("The price of 1",chaatrqd,"counted a single plate is : ",price)
        print("")
        con=str(input("Do you want to proceed with the Order (Y/N) : "))
        print("")
        if con.lower()=="y":
            print("..Customer Details Please..".center(120))
            naam=str(input("Complete Name : "))
            mail=str(input("Email : "))
            no=int(input("Contact Number : "))
            print("")
            print("..Order Details..".center(120))
            qty=int(input("Enter the number of plates you want to eat : "))
            if qty<=available:
                    from datetime import date
                    today=date.today()
                    date=today.strftime("%d %m %Y")
                    print("")
                    print("Total Amount To Be Paid : ",(price*qty))
                    print("")
                    print("..Order Has Been Placed Successfully..".center(120))
                    print("..Thank You For Shopping With YumYum Chaat Centre..".center(120))
                    inv3=+1
                    inv1=open(r"C:\Users\ADMIN\Desktop\Apna Folder\Apna Text 1.txt","w")
                    inv1.write(str(inv3))
                    inv1.close()
                    invl=[]
                    invl.append("YumYum Chaat Centre".center(120)+"\n")
                    invl.append("Block B2,Indian Complex,Vaishali".center(120)+'\n')
                    invl.append(""+'\n')
                    invl.append("Order Date : ")
                    invl.append(date+'\n')
                    invl.append("Order Number : ")
                    invl.append(str(inv3)+'\n')
                    invl.append(""+'\n')
                    invl.append(""+'\n')
                    invl.append("Customer Details".center(120)+'\n')
                    invl.append("Name : ")
                    invl.append(naam+'\n')
                    invl.append("Email : ")
                    invl.append(mail+'\n')
                    invl.append("Phone Number : ")
                    invl.append(str(no)+'\n')
                    invl.append("Order Details".center(120)+'\n')
                    invl.append("Chaat Choice : ")
                    invl.append(chaatrqd+'\n')
                    invl.append("Number Of Plates : ")
                    invl.append(str(qty)+'\n')
                    invl.append(""+'\n')
                    invl.append(""+'\n')
                    invl.append("Total Amount Paid : ")
                    invl.append(str(price*qty))
                    new=str(inv3)
                    file=open(r"C:\Users\ADMIN\Desktop\Apna Folder\invoice_"+new+"_"+naam+".txt","w")
                    file.writelines(invl)
                    file.close()
        elif con.lower()=="n":
            print("..The Order has been Cancelled..".center(120))
            print("..Thank You For Visiting YumYum Chaat Centre..".center(120))
            break
        else:
            print("")
            print("..Enter a valid input..".center(120))
            break
        break
while True:
    user=str(input("Enter Your Username : "))
    pwd=str(input("Enter Your Password : "))
    if user=="mcsdwarka" and pwd=="mcsdwarka":
        while True:
            try:
                sql_cursor.execute("create database if not exists tikku")
                print("")
                cont=0
            except:
                print("")
                cont=1
            finally:
                sql_cursor.execute("use tikku")
            print("What Do You Want To Do ???")
            print("1. Load Default Menu")
            print("2. Order A Chaat")
            print("3. Set New Prices For Each Default Item")
            print("4. Amend Menu")
            print("5. Display Menu")
            print("6. Delete Menu")
            print("")
            menu=int(input("Enter Choice --> "))
            if menu==1:
                sql_cursor.execute("drop database if exists tikku")
                sql_cursor.execute("create database if not exists tikku")
                sql_cursor.execute("use tikku")
                sql_cursor.execute('create table if not exists yummy(Name_Of_Chaat varchar(44), Price_In_Rupees integer)')
                sql=("insert into yummy values(%s,%s)")
                val=[
                ("Paani Puri",20),
                ("Paani Puri Family Pack",120),
                ("Dahi Puri",40),
                ("American Corn Dahi Puri",50),
                ("Sev Puri",35),
                ("Ragda Puri",40),
                ("Masala Puri",20),
                ("Paneer Tikki Chaat",50),
                ("Aaloo Tikki Chaat",40),
                ("Aaloo Tikki Chhole",50),
                ("Aaloo Chaat",40),
                ("Banarasi Tamaatar Chaat",40),
                ("Navratan Paapadi Chaat",50),
                ("Paalak Patta Chaat",40),
                ("Basket Chaat",60),
                ("Katori Chaat",50),
                ("Raaj Kachori",60),
                ("Khastaa Kachori",20),
                ("Khastaa Kachori Chaat/Chhole",40),
                ("Samosa",15),
                ("Samosa Chaat/Chhole",40),
                ("Paapad Chhole",40),
                ("Dahi Wadaa",40),
                ("Special Gulaab Jaamun 2 Pcs",40)
                ]
                sql_cursor.executemany(sql, val)
                sql_connector.commit()
                print("")
                print("..Default Menu Has Been Loaded..".center(120))
                print("..Either Check Server Or Display Here..(Press 5)..".center(120))
                continue
            elif menu==3:
                print("Enter the price of given items only. If not available, please put price equal to not available".center(120))
                val=[]
                sql_cursor.execute("drop database if exists tikku")
                sql_cursor.execute("create database if not exists tikku")
                sql_cursor.execute("use tikku")
                sql_cursor.execute("create table yummy(Name_Of_Chaat varchar(44), Price_In_Rupees varchar(44))")
                for y in ["Paani Puri","Paani Puri Family Pack","Dahi Puri","American Corn Dahi Puri","Sev Puri","Ragda Puri","Masala Puri",\
                "Paneer Tikki Chaat","Aaloo Tikki Chaat","Aaloo Tikki Chhole","Aaloo Chaat","Banarasi Tamaatar Chaat","Navratan Paapadi Chaat",\
                "Paalak Patta Chaat","Basket Chaat","Katori Chaat","Raaj Kachori","Khastaa Kachori","Khastaa Kachori Chaat/Chhole",\
                "Samosa","Samosa Chaat/Chhole","Paapad Chhole","Dahi Wadaa","Special Gulaab Jaamun 2 Pcs"]:
                    pc=input("Enter the Price of "+y+" : ")
                    val.append((y,pc))
                sql=("insert into yummy values(%s,%s)")
                sql_cursor.executemany(sql, val)
                sql_connector.commit()
                print("")
                print("..New Menu With Default Items Created..".center(120))
                print("..Check Your Server Or Display Here..(Press 5)..".center(120))
                continue
            elif menu==2:
                main()
                continue
            elif menu==4:
                edit()
                continue
            elif menu==5:
                sql_cursor.execute("select * from yummy")
                recs=sql_cursor.fetchall()
                print("Total Items = ",sql_cursor.rowcount)
                print("")
                for row in recs:
                    print("Name Of Chaat = ",row[0])
                    print("Price In Rupees = ",row[1])
                    print("")
            elif menu==6:
                sql_cursor.execute("drop database tikku")
                print("..Database Deleted..".center(120))
                print("Check your Server Or Display Here..(Press 5)..".center(120))
            else:
                print("..This is an Invalid Choice .. Plese Try Again...".center(120))
                continue
        break
    elif user=="mcsdwarka":
        print("..Wrong Password !..".center(120))
    else:
        print("..Wrong Username/Password !..".center(120))
