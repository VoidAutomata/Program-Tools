import math

num = 1234
loop = 0
digits = int(math.log10(num))+1

while loop < digits:
    loop = loop+1
    print(math.floor(num/10**(digits-loop)) % 10)