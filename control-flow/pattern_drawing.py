PatternSize = int(input("Enter the size of the pattern: "))
row = 0
while PatternSize > row:
    for i in range(PatternSize):
        print ("*", end = " ")
    print()
    row += 1

