
#Función para ingresar al sistema 
def login(usuario,bd):
    #Verifico que la exitencia
    if usuario in bd:
        clave = int(input("Ingrese su contraseña: "))
        #Valido contraseña
        while bd.get(usuario) != clave: 
            print("Contraseña incorrecta. Por favor intente de nuevo...")
            clave = int(input("Ingrese su contraseña: "))
        #Bienvenida
        print(f"Hola {usuario}, bienvenidx de nuevo! ")
        return True
    #Error en el ingreso
    else:
        print("Usuario no encontrado, registrese!")
        return False

#Función Menú para mostrar datos
def ver_datos(usuario, bd):
    selec = int(input("\n > 1. Ver mis datos.\n > 2. Ver lista de usuarios \n > 3.Ver datos de otros usuarios \n > 0.Salir\n Seleccione una opción: "))
    while selec !=0:
        if selec == 1:   
            print(f"{usuario}, su clave es {bd[usuario]}")
        elif selec == 2:
            print(list(bd))
        else:
            print("Error. ¡No puede ver los datos de otros usuarios!")
        selec = int(input("\nSeleccione una opción: "))
    #Saliendo del menú   
    print("Saliendo del sistema...")
    return True

#Validación nombre de usuario
def validacion_us(bd):
    error=1
    nombre= input("Ingrese un nuevo nombre de usuario en minusculas: ")
    while error !=0:
        
        if nombre.lower().capitalize() in bd:
            print("El nombre ya existe")
            error=1
            nombre= input("Ingrese un nuevo nombre de usuario en minusculas: ")
        else:
            error=0
            
    return nombre.lower().capitalize()


#Validación contraseña
def validacion_nro(clave_num):
    while not clave_num.isdigit():
        clave_num= input("(X) Error. La contraseña debe contener solo números.\n Intente de nuevo: ")
    return clave_num

    

#Función para crear un usuario
def crear_usuario(usuario,bd):
    #Solicito nombre de usuario

    #Verifico que no se repita el usuario y el nombre sea correcto
    nuevo_us = validacion_us(bd)

    #Solicito contraseña con la siguiente condición: debe ser numerica. 
    nuevo_us_clave= int(input("Ingrese una contraseña numérica: "))

    #Valido contraseña
    nuevo_us_clave =int(validacion_nro(str(nuevo_us_clave)))

    #Confirmación de claves 
    confirmacion = int(input("Ingrese la contraseña nuevamente para confirmar: "))
    while nuevo_us_clave != confirmacion:
        print("(X) Las contraseñas no coinciden \n")
        confirmacion = int(input("Ingrese la contraseña nuevamente para confirmar: "))
    
    print( "Usuario creado correctamente!\n>>Ingresando al sistema...")
    
    #Devuelvo usuario-clave para agregar al diccionario
    return nuevo_us,nuevo_us_clave


    

#Inicio creando diccionario 
bd = {'Julieta':19981002,'Camila':20001007,'Octavio':20040824}

usuario = input("Ingrese nombre de usuario: ")

while not (login(usuario,bd)):
    usuario,clave= crear_usuario(usuario,bd)
    #Añado nuevo valor en diccionario
    bd[usuario] = clave
    break
#Acceso al menú de datos
if ver_datos(usuario,bd):
    #Saliendo del sistema
    print("Hasta la próxima!")
    
