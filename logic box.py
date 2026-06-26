print("Welcome to the pattern Generator and NumberAnalyzer!")
while True:
    print("Select an option:")
    print("1.Generate a pattern")
    print("2.AnalyZe a range of Number")
    print("3.Exit")
    a = int(input("Enter your choice:")) 
    if a<0:
        print("Please Enter the positive Number")
    match a:
        case 1:
            n = int(input("Enter the number of rows for  the pattern:"))
            if n<0:
                print("Please Enter the positive row range number")
            for i in range(1,n+1):
                for j in range(1,i+1):
                    print("*",end="")
                print()
        case 2:
            a = int(input("Enter the start of the range:"))
            b= int(input("Enter the end of the range:"))
            if a <= -1 or b <= -1: 
                print("Please Enter positive Numbers of a & b ")
                continue
            sum = 0
            for i in range(a,b+1):
                sum+=i
                if i%2==0:
                    print(f"Number {i} is Even")
                else:
                    print(f"Number{i} is Odd")
            print(f"sum of all Number between {a} and {b} = {sum}")
        case 3:
            print(f" Exiting the program. goodbye! ")
            break
        case _:
            print("Invalide Input,please try again")