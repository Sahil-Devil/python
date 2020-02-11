print("Enter 1 for ADD")
print("Enter 2 for Subtract")
print("Enter 3 for Multiply")
print("Enter 4 for Divide")
print("Enter 5 for Remainder")

a=int(input("Enter Your Choice:--"))
if a>1 and a<5:
    print(" Entered Wrong Choice")

b=int(input("Enter 1st Number:--"))
c=int(input("Enter 2nd Number:--"))

if a==1:
    d=b+c
elif a==2:
    d=b-c
elif a==3:
    d=b*c
elif a==4:
    d=b/c
elif a==5:
    d=b%c


print("Your Answer is :-")
print(d)


print("THANKS FOR USING THIS PROGRAM")