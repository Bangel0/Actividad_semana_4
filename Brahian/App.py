"""Creación de ejercicio libre"""

# Calculadora de gastos mensuales

print(" Calculadora de gastos mensuales ")
print("---------------------------------")

# EL CLIENTE INGRESARA EL VALOR O SU INGRESO MENSUAL 

ingresp = float(input("Ingrese el valor del ingreso mensual: ")) #Esta linea de codigo se realiza para el ingreso en consola del cliente

# Ingresar el nombre del gasto ejemplo: Ropa, comida, juegos, etc...

gastos = {}  # En esta linea de codigo usare un dicionario para almacenar las categorias y esto es igual Valor

while True:

    categoria = input("Ingrese el nombre del gasto (o escriba 'Terminar' para salir):  ")
    if categoria.lower() == 'Terminar':
        break 
