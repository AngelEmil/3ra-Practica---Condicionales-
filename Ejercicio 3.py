# 3. Pedir tres números por teclado e imprimir el mayor de ellos solamente

T = int(input("digite otro numero "))
P = int(input("digite otro numero "))
M = int(input("digite otro numero "))


if T > P and T > M:
    print(f"El mayor es {T}")
elif P > T and P > M:
    print(f"El mayor es {P}")

else:
    M > T and M > P
    print (f"El mayor es {M}")