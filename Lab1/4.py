num=int(input("Enter a number : "))
if(0<num<=100):
    print("Positive number")
elif(-100<=num<0):
    print("Negative number")
elif(num==0):
    print("Zero")
else:
    print("Invalid number")
