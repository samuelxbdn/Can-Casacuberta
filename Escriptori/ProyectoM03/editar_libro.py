def editar_libro():
    libro=input("Escribe el titulo del libro que deseas editar de la lista\n")
    archivo=open("llibres.txt","r+")
    lista=(archivo.readlines())
    for linea in lista:
        datos=linea.split('|')
        enlista=libro.lower() == datos[0].lower()
        if enlista==True:
            concepto=input("Indica el concepto a editar: Nombre del libro(1),Nombre del autor(2) o Año de publicación(3)\n")
            if int(concepto)==1:
                nombre=input("Introduce el nombre correcto del libro\n")
                nombre=nombre.title()
                datos=linea.split('|')
                datos[0]=nombre
                modificado='|'.join(datos)
                lista.remove(linea)
                lista.append(modificado)
                archivo=open("llibres.txt","w")
                archivo.writelines(lista)
                print("Nombre de libro modificado correctamente")

            if int(concepto)==2:
                nombre=input("Introduce el nombre correcto del autor\n")
                nombre=nombre.title()
                datos=linea.split('|')
                datos[1]=nombre
                modificado='|'.join(datos)
                lista.remove(linea)
                lista.append(modificado)
                archivo=open("llibres.txt","w")
                archivo.writelines(lista)
                print("Nombre del autor modificado correctamente")

            if int(concepto)==3:
                publicacion=input("Introduce el año correcto de publicación\n")
                datos=linea.split('|')
                datos[2]=publicacion
                modificado='|'.join(datos)
                lista.remove(linea)
                lista.append(modificado)
                archivo=open("llibres.txt","w")
                archivo.writelines(lista)
                print("Año de publicación del libro modificado correctamente")
                               
editar_libro()