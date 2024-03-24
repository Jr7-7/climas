# diccionario
informacion_personal = {
'nombre' : 'Johana',
    'edad': 18,
    'ciudad': 'Loreto',
    'provincia': 'Orellana',
    'N° CDL': '2200280812',
    'telefono': '0994418369',
    'direccion': 'barrio el triunfo',

}
print(informacion_personal)
# Modificar ciudad
informacion_personal['ciudad'] = 'Tena'
print(informacion_personal)
#Agregar provincia
informacion_personal ['profesion']= 'Estudiante'
print(informacion_personal)
# Modificar ciudad 2
informacion_personal['ciudad'] = 'cuenca'
print(informacion_personal)
if 'direccion' in informacion_personal:
    print('direccion existente')
else:
    print('direccion no existente')
# Eliminar edad
informacion_personal.pop('ciudad')
print(informacion_personal)