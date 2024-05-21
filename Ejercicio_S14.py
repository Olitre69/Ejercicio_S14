personas = []

while True:
    print('''
    1. Agregar personas a la agenda.
    2. Guardar datos en un archivo.
    ''')
    opcion = input('Ingrese una opcion: ')
    if opcion == "1":

        contacto = []
        while True:
            nombre = input("Introduce tu nombre: ")
            apellido =  input("Introduce tu apellido: ")
            if nombre == "":
                print("No has introducido tu nombre")
            elif apellido == "":
                print("No has introducido tu apellido")
            else:
                contacto.append(nombre)
                contacto.append(nombre)
                break
        while True:
        # intenta convertir cualquier valor que introduzca el usuario en un entero, si no es entero dara un ValueError
            try:
                edad = int( input("Introduce tu edad: "))
                break
            except ValueError:
                print("Desbes ingresar un número")

        correo =  input("Introduce tu correo: ")
        contacto.append(correo)

        while True:
            try:
                telefono =  input("Introduce tu telefono: ")
                int(telefono)
                contacto.append(telefono)
                break
            except ValueError:
                print("Desbes ingresar un número")
            
        personas.append(contacto)   #lista de listas

    elif opcion =='2':
        with open('agenda.txt', 'w') as f_agenda:
            for persona in personas:
                f_agenda.write(f'{persona[0]} Edad: {persona[1]} Correo: {persona[3]} Telefono: {persona[4]}\n')
        print('datos guardados en agenda.txt')
        break
                           
    else:
        print('Opcion invalida')
        print('volver a intentarlo')
                           
