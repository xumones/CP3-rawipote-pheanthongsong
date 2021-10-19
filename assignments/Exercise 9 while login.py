User = input
Pass = input
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