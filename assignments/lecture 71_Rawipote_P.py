menuList = []
priceList = []
def calculate():
    total = 0
    for price in range(len(priceList)):
        total += int(priceList[price])
    print("total =",total)
def showbill():
    print("----My food----")
    for number in range(len(menuList)):
        print(menuList[number],":",priceList[number])
    print("---------------")
    print(calculate())

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
showbill()