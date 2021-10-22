print("---vat calculator---")
totalprice = int(input("total :"))
def vatcalculate(totalprice):
    result = totalprice + (totalprice * 7/100)
    return result
print(vatcalculate(totalprice))