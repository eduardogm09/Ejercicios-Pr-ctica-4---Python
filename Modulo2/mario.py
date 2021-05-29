n = int(input("Introduzca la altura del triángulo: "))
for i in range(n):
    for j in range(i-1):
        print("*", end="")
    print("")