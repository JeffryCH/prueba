# Solicitar la categoría del colaborador
categoria = int(input("Ingrese la categoría del colaborador (1-4): "))

# Solicitar el salario actual
salario_actual = float(input("Ingrese el salario actual: "))

# Calcular el porcentaje de aumento
if categoria == 1:
    porcentaje = 0.10
elif categoria == 2:
    porcentaje = 0.12
elif categoria == 3:
    porcentaje = 0.15
elif categoria == 4:
    porcentaje = 0.20

# Calcular el aumento y el nuevo salario
aumento = salario_actual * porcentaje
nuevo_salario = salario_actual + aumento

# Mostrar el nuevo salario
print("El nuevo salario es:", nuevo_salario)
