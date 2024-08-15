numero  = int(input("Digite um valor para ver a sua tabuada: "))
print("Esta é a tabuada do", numero)
for valor in range(1, 11, 1):
    print("\t", numero, "x", valor, "=", numero*valor)