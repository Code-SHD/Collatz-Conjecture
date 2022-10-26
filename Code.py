num = input("number: ")

def Collatz_Conjecture(n):
    n = int(n)
    if (n % 2 == 0): n = n / 2
    else: n = n * 3 + 1
    return n

while True:
    num = Collatz_Conjecture(num)
    print(num)
    if num == 1: break
    else: continue