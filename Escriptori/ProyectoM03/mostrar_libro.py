def mostrar_libro():
    flag=False
    nombre=input("Escribe el titulo o el autor al que quieres acceder\n")
    archivo=open("llibres.txt","r")
    lista=(archivo.readlines())
    for libro in lista:
        datos=libro.split('|')
        enlista=libro.lower() == datos[0].lower() or datos[1].lower()
        if enlista==True:
            print(libro)
            flag=True

    if flag==False:
        print("Ese libro o autor no consta en nuestra lista")

mostrar_libro()