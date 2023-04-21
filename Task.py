
print("Введите числ от 0 до 1000:")

def IsPrime(n):
    while True:
        try:
            if n < 0 or n > 1000:
                print("Введите число до 1000")
            break
        except ValueError:
            print("все ок")

    k = 2
    p = 0
    while pow(n, 0.5) >= k > 1:
        if not n % k != 0:
            p += 1
        k += 1
    return p == 0

n = int(input())
if IsPrime(n):
    print("True")
else:
    print("False")


