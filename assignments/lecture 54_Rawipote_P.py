def login():
    print("------login------")
    User = input("Username :")
    Pass = input("Password :")
    print("-----------------")
    if User != "admin" or Pass != "123":
        print("please try again")
        while User != "admin" or Pass != "123":
            print("------login------")
            User = input("Username :")
            Pass = input("Password :")
            print("-----------------")
    print("done")
    showMenu()
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("3. exit")
    print("-----------------")
    menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        vatCalculator()
    elif userSelected == 2:
        priceCalculator()
    elif userSelected == 3:
        exit()
def vatCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalprice = price1 + price2
    print("------------------")
    print("1. vat only")
    print("2. total")
    print("------------------")
    vat = 7
    userselect = int(input(">>"))
    if userselect == 1:
        print("-----------------")
        print("vat =", totalprice * vat / 100)
        showMenu()
    elif userselect == 2:
        print("-----------------")
        print("total =", totalprice + (totalprice * vat / 100))
        showMenu()
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    print("-----------------")
    print("total", result)
    return showMenu()
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalprice = price1 + price2
    return vatCalculator(totalprice)
def exit():
    print("----thank you----")

print(login())