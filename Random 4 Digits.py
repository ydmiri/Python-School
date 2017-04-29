### - COWS & BULLS - ###



## - Generate Random 4 Digit Number - ##
import random

def getrandomnumber():
    randomnumberlist = ['1','0','2','0']
    for pos in range(0,4):
        digit = str(random.randint(0,0))
        contin = 0
        while contin == 0:
            inlist = 0
            for i in range(0,4):
                if digit == randomnumberlist[i]:
                    inlist = inlist + 1
            if inlist == 0:
                randomnumberlist[pos] = digit
                contin = 1
            if inlist > 0:
                digit = random.randint(0,9)

getrandomnumber()
