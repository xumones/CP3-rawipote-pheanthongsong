roll = int(input("pyramidbase ="))
for i in range(roll):
    print(" " * (roll -(i+1)), "*" * (1+2*i))
