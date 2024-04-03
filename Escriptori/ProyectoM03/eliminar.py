def borrar ():
    libro=input("Escribe el titulo que deseas eliminar de la lista\n")
    archivo=open("llibres.txt","r")
    lista=(archivo.readlines())
    flag=False
    for linea in lista:
        datos=linea.split('|')
        if libro.lower() == datos[0].lower():
            flag=True
            print ("\n",linea)
            confirmacion=input("¿Estás seguro de querer borrarlo? (s/n)\n")
            if confirmacion== "s":
                lista.remove(linea)
                print("libro borrado de la lista correctamente\n")
                break
    if flag==False:
        print("Ese libro no se encuentra en nuestra lista")
    archivo=open("llibres.txt","w")
    archivo.writelines(lista)
borrar()
