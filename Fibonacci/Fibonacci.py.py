def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b)
    else:
        print(a, b, end=", ")
        for i in range(2, n):
            c = a + b
            print(c, end=", ")
            a = b
            b = c
    print("\n")

# Solicitar al usuario la cantidad de términos
num_terms = int(input("Ingrese la cantidad de términos: "))

# Imprimir los términos de la serie de Fibonacci
fibonacci(num_terms)
