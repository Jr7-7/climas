

print(f'Creamos una función llamada calcular_descuento que tome dos parámetros: el monto total de la compra y un valor predeterminado para el porcentaje de descuento')


print(f'--------------CUENTA A PAGAR---------')
def calcular_descuento(monto_total, porcentaje_descuento=8):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamada a la Función
monto_compra1 = 568.38
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

print('\n Resultados: 1 ')

print(f" Monto total de compra es: == > ${monto_compra1} \n")
print(f" El Descuento que se aplica en la compra es: ==>  {descuento1:.2f} \n ")
print(f" Monto final a pagar por el cliente: ==>  ${monto_final1:.2f} \n")


# Llamada a la Función

print('\n  Resultados: 2 ')


monto_compra2 = 50.10
porcentaje_descuento2 = 18
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final_2 = monto_compra2 - descuento2

print(f"Monto total de la compra  es: ====> ${monto_compra2} \n ")
print(f"Porcentaje de descuento; ====>  {porcentaje_descuento2:}% \n ")
print(f"Descuento aplicado: ===> ${descuento2:.2f} \n")
print(f"Monto final a pagar por el cliente:====> ${monto_final_2:.2f} \n")

print('\n gracias por visitar nuestra tienda ')