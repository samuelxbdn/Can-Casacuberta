def mostrar_libro():
    flag=False
    nombre=input("Escribe el titulo al que quieres acceder\n")
    archivo=open("llibres.txt","r")
    lista=(archivo.readlines())
    for libro in lista:
        datos=libro.split('|')
        if nombre.lower() == datos[0].lower():
            print(libro)
            flag=True
    if flag==False:
        print("Ese libro no consta en nuestra lista")

mostrar_libro()