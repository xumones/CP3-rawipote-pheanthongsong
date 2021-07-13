print("------------------")
print("welcome to popmart")
print("------------------")
USER = input("Username :")
PASS = input("Password :")
if USER == "custumer" and PASS == "1234" :
    print("welcome back!")
    print("-------------------")
    print("    popmart menu   ")
    print("-------------------")
    print("1)pineapple with strawberry / 150 THB per each ")
    print("2)breakfast ham with bacon  / 70 THB per each")
    userselected = int(input("select >>"))
    if userselected == 1 :
        amount = int(input("amount >>"))
        total = 150 * amount
    elif userselected == 2 :
        amount = int(input("amount >>"))
        total = 70 * amount
    print("-------------------")
    print("    total price    ")
    print("-------------------")
    print("total", "=", total)
    print("-------------------")
    print("     thank you     ")
else :
    print("your Username or password is not correct")