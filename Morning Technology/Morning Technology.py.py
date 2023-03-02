import getpass
# Calcular los precios, descuentos e impuestos de los productos seleccionados


codigo = getpass.getpass("Ingrese su código de autenticación: ")

# Lista de códigos autorizados
codigos_autorizados = ["abc123", "def456", "ghi789"]

    

    # Verificar si el código es autorizado
if codigo in codigos_autorizados:
    # Si el código es autorizado, preguntarle que productos quiere comprar
    print("¿Que desea comprar? \n")
    cantidadTeclado = int(input("¿Cuántos Teclados Gamer desea?"))
    cantidadTarjetaVideo = int(input("¿Cuántas Tarjetas de Video desea?"))
    cantidadMonitorLCD = int(input("¿Cuántos de MonitoresLCD desea?"))
    cantidadTarjetaMadre = int(input("¿Cuántas Tarjeta Madre desea?"))
    print("Resumen de su compra:")
    #variable de cantidad de productos
  
    #funcion para calcular el precio de productos
    precioTeclado = 300
    precioTarjetaVideo = 1000
    precioMonitorLCD = 755
    precioTarjetaMadre = 399
    #Subtotal
    subtotal = cantidadTeclado * precioTeclado + cantidadTarjetaVideo * precioTarjetaVideo + cantidadMonitorLCD * precioMonitorLCD + cantidadTarjetaMadre * precioTarjetaMadre
   #Descuento para precio total
    descuento = ()
    descuento = 0
    if cantidadTeclado >= 2:
        descuento -= cantidadTeclado * 300 * 0.15
        precioTeclado = cantidadTeclado * 300 - descuento
    if cantidadTarjetaVideo >= 1:
        descuento -= cantidadTarjetaVideo * 1000 * 0.8
        precioTarjetaVideo = cantidadTarjetaVideo * 1000 - descuento
    if cantidadMonitorLCD >= 2 or cantidadTarjetaMadre >= 1:
        descuento -= cantidadMonitorLCD * 755 * 0.5
        precioMonitorLCD = cantidadMonitorLCD * 755 - descuento 
    if (cantidadTeclado >= 1) and (cantidadTarjetaVideo >= 1) and (cantidadMonitorLCD >= 2):
        descuento -= cantidadTarjetaMadre * 399 * 0.3
        precioTarjetaMadre = (cantidadTeclado >= 1) and (cantidadTarjetaVideo >= 1) and (cantidadMonitorLCD >= 2) * 399 - descuento
    if cantidadTarjetaMadre >= 3:
        descuento -= cantidadTarjetaMadre * 399 * 0.3
        precioTarjetaMadre = cantidadTarjetaMadre * 399 - descuento
    descuentoTotal = subtotal + descuento


    # Calcular impuesto para el precio total
    if cantidadTarjetaMadre + cantidadTeclado + cantidadMonitorLCD + cantidadTarjetaVideo >= 10:
        impuesto = descuentoTotal * 0.5
    else:
        impuesto = descuentoTotal * 0.13
        descuentoTotal += impuesto
    # Precio total
    precioTotal = descuentoTotal + impuesto
    print("Subtotal ${}\nTotal descuento ${}\nTotal con impuesto ${}".format(subtotal, descuentoTotal, precioTotal))
    print("¡MUCHAS GRACIAS POR PREFERIRNOS!")
else:
    # Si el código no es autorizado, decirle que código no es válido o incorrecto
    print("Código no válido o incorrecto.")
