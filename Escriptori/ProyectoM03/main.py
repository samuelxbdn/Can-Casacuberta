import funciones
flag=False
user=funciones.login()

print("\nBienvenido a la biblioteca Can Casacuberta",user,"\n")
while flag==False:
    accion=input("Introduce los número correspondientes para realizar dichas acciones:\n1.Mostrar todos los libros.\n2.Mostrar la información de un libro.\n3.Añadir un libro.\n4.Eliminar un libro.\n5.Editar un libro.\n6.Salir.\n\n")

    if accion=="1":
        funciones.listar_todos()
    elif accion=="2":
        funciones.mostrar_libro()
    elif accion=="3": 
        funciones.añadir_libro()
    elif accion=="4":
        funciones.borrar()
    elif accion=="5":
        funciones.editar_libro()
    elif accion=="6":
        print("Que pase un buen día.\n")
        flag=True
    else:
        ("Debes elegir uno de los número anteriores (1-6).\n")
