# crea un nuevo archico llamado my_notas.txt.

my_notes = open ('my_notes.txt', 'w')

 # Metodo write(): escribir una linea a la vez
my_notes.write("paso 1: salir del colegio. \n ")
my_notes.write("paso 2: ir al parque con mis amigos. \n ")
my_notes.write("paso 3: subir a un bus. \n")



# Metodo writelines(): escribir una lista de lineas
lineas =("paso 4: llegar a casa.\n" , "paso 5: ver videos por distracion. \n")
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
print('Metodo 2:')
print('___________________')
print('paso 1: salir del colegio ')
print('paso 2: cojer el bus ')
print('paso 3: llegar a casa ')
print('paso 4: almorzar ')
print('paso 5: realizar las tareas ')






