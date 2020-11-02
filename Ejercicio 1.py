# 1-- Pedir dos números por teclado y decir cual es mayor.

M1 = int(input("digite un numero "))
M2 = int(input("digite otro numero "))

if M1 > M2: 
    print (f"El mayor es {M1}")
elif M2 > M1:
    print (f"El mayor es {M2}")
else: 
    M1 = M2
    print ("ambos son iguales")