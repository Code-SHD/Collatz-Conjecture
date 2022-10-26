num = 295147905179352833364
num1 = 295147905179352833364

def Collatz_Conjecture(n):
    n = int(n)
    if (n % 2 == 0): n = n / 2
    else: n = n * 3 + 1
    return n

while True:
    num = Collatz_Conjecture(num)
    #print(num)  #print process
    if (num == 1):
        print(num1, "Passed ⭕ ")
        num = num1 + 1
        num1 = num
        continue