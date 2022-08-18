for i in range(4):
    print(i * "   " + "... Jenkins building ...")

print("\nBuilding seems okay.\n")
    
ending = ""

for i in range(4):
    if i == 3:
        ending = " Jenkins World!!\n"
    else:
        ending = "\n"
    print( (i + 1) * " Hello,", end=ending)

print("\nBuilding stage done.\n")

