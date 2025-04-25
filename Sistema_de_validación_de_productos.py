# Factura de compra de un producto.
# Mensaje de entrada a la tienda.
print (     "''''''''''''''''''''''''''''''''''''''''''")
print (     "''                                      ''")
print (     "''       EL MERCADITO DEL BARRIO!       ''")
print (     "''                                      ''")
print (     "''''''''''''''''''''''''''''''''''''''''''")

# Se solicitan los datos personales del usuario. 
nombre = input("¿Cual es tu nombre completo?\n")
print(f"¡Es un placer {nombre}!")
fecha = input(f"por favor ingresa la fecha actual: (dd/mm/yyyy) \n")


#Definimos la variable para el menú.
def mostrar_menu():

    print("Elija una opción de descuento:")
    print("1. 10% de descuento")
    print("2. 15% de descuento")
    print("3. 20% de descuento")
    print("4. 25% de descuento")
    print("5. 50% de descuento")
    print("6. Ingresar otro porcentaje")
    print("7. No calcular valor (Salir)")

# Se solicitan los datos del producto comprado.
producto = input("\nPor favor, digita el nombre del producto que has comprado \n")



while True: 
         try: 
                 precio = float(input("\nIngrese el precio del producto: \n$"))
                 if precio < 0: 
                         print("*****El precio no debe ser negativo. Intenta de nuevo.*****")
                         continue
                 break # Si el precio es válido, salimos del bucle.
         except ValueError: # Si ocurre un error de valor, se maneja aquí.
                 print("El precio no puede ser negativo. Por favor, ingrese un precio válido.") #Este mensaje se mostrará en caso de que el precio sea negativo.
                 
mostrar_menu()
opcion = int(input("\nIngrese el número de la opción deseada (1-7): "))     


#Se asigna una condicion para poder hacer uso del menú y aplicar el descuento.
if 1 <= opcion <= 5:
        porcentajes = {1: 10, 2: 15, 3: 20, 4: 25, 5: 50}
        descuento = porcentajes[opcion]
elif opcion == 7:
        descuento = 0
elif opcion == 6:
        descuento = float(input("Ingrese el porcentaje de descuento personalizado: "))
        if descuento < 0 or descuento > 100:   #Condicion para que el descuento no sea negativo o mayor a 100.
                 print("El porcentaje de descuento no puede ser negativo o mayor a 100. Se aplicará un descuento del 0%.")
                 descuento = 0      
               
        
#Se definen las variables para hacer el calculo del descuento.
monto_descuento = (precio * descuento) / 100
precio_final = precio - monto_descuento


# Se imprime el mensaje de salida.
print (     "''''''''''''''''''''''''''''''''''''''''''")
print (     "''                                      ''")
print (     "''       EL MERCADITO DEL BARRIO!       ''")
print (     "''                                      ''")
print (     "''''''''''''''''''''''''''''''''''''''''''")
print (     "'''''''     FACTURA DE COMPRA    '''''''''")

print(f"Nombre: {nombre}")
print(f"Fecha: {fecha}")
print(f"producto:       precio:        Monto descontado({descuento}%):")
print(f"{producto}        ${precio}          ${monto_descuento:.2f}") 
print(f"\nPrecio final: ${precio_final:-.2f}")
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print("¡GRACIAS POR SU COMPRA!")