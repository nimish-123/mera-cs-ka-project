l = []
def push():
    print("===============================================")
    while True:
        add = input("Enter the number which you want to push in stack : (Enter <no> to mark the end of stack) : ")
        if add != "no":
            l.append(add)
            print("STACK = ")
            top = len(l)-1
            print(l[top],"<-- Top Element")
            for i in range(top-1,-1,-1):
                print(l[i])
        elif add == "no":
            print("STACK = ")
            top = len(l)-1
            print(l[top],"<-- Top Element")
            for i in range(top-1,-1,-1):
                print(l[i])
            main()
def pop():
    if len(l)==0:
        print("Stack underflow ho gayi hai..")
        main()
    else:
        print("===============================================")
        print("the number",l.pop(),"is popped")
        if len(l)==0:
            print("Stack is empty right now..")
        elif len(l)!=0:
            print("STACK = ")
            top = len(l)-1
            print(l[top],"<--Top Element")
            for i in range(top-1,-1,-1):
                print(l[i])
        main()
def main():
    print("===============================================")
    print("STACK MANAGEMENT SERVICE")
    print("1. Push and display simultaeously ")
    print("2. Pop and display simultaeously")
    print("3. Display stack")
    print("3. Exit")
    ch=int(input("Enter the choice (1-3) : "))
    print("===============================================")
    if ch==1:
        push()
        main()
    elif ch==2:
        pop()
    elif ch==3:
        exit()
    else:
        print("Andhe ! 1 se 3 tak daalna thaa..")
        print("Phirse daal choice...")
        main()
main()
