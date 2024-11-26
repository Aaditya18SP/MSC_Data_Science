# Menu driven
loop_continuer = True
while(loop_continuer):
    option_selected = int(input("Please select the required operator\n 1. Arithmetic\n 2.Assignment\n 3. Logical \n 4.Comparison\n 5. Bitwise \n 6.Membership \n 0.Exit\nEnter here:"))

    if(option_selected > 6 or option_selected < 0):
        print("Please select the correct option and try again")
    match option_selected:
        case 0:
            loop_continuer = False
            print("==============\n")
            print("Exiting..")
            break
        case 1:
            print("==============\n")
            a = int(input("Enter num1:"))
            b = int(input("Enter num2:"))
            print(" %d + %d = %d" % (a, b, a+b))
            print(" %d - %d = %d" % (a, b, a-b))
            print(" %d * %d = %d" % (a, b, a*b))
            print(" %d / %d = %d" % (a, b, a//b))
            print(" %d // %d = %f" % (a, b, a/b))
            print(" %d ** %d = %d" % (a, b, a**b))
            print(" %d %% %d = %d" % (a, b, a % b))
            break
        case 2:
            print("==============\n")
            break
        case 3:
            print("==============\n")
            break
        case 4:
            print("==============\n")
            break
        case 5:
            print("==============\n")
            break
        case 6:
            print("==============\n")
            break
        case 7:
            print("==============\n")
            break
        case _:
            break


# Assignment operators



# Arithmetic operators

# Logical

# Membership

# Comparison operators

# Bitwise operators
