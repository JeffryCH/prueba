import getpass

# Solicita credenciales al usuario
username = input("Ingresa tu nombre de usuario: ")
password = getpass.getpass("Ingresa tu contraseña: ")

# Validar credenciales
if username == "admin" and password == "admin123":
    print("Acceso autorizado")
else:
    print("Usuario o Contraseña invalida")
