# crea un nuevo archico llamado my_notas.txt.

my_notes = open ('my_notes.txt', 'w')

 # Metodo write(): escribir una linea a la vez
my_notes.write("paso 1: usuario: johana grefa. \n ")
my_notes.write("paso 2: num.c:2200984786. \n ")
my_notes.write("paso 3: edad: 34. \n")



# Metodo writelines(): escribir una lista de lineas
lineas =("paso 4: color: morado.\n" , "paso 5: profecion: estudiante. \n")
my_notes.writelines(lineas)


# Abre el archivo my_notes.txt.
my_notes = open('my_notes.txt','r')
# Lee el contenido del archivo paso por paso utilizando el metodo edecuado.

# Metodo 1. read()
my_notes = open('my_notes.txt','r')
print("Metodo 1:")
print('_________________')
print(my_notes.read())
my_notes.close()

 #Metodo 2. readlines()
my_notes = open('my_notes.txt','r')
print('Metodo 2: readlines()')
print('___________________')
for paso in my_notes.readlines():
    print(paso.rstrip('\n'))
    my_notes.close()







