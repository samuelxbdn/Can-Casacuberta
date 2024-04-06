def añadir_libro():
    libro=input("Escribe el titulo del libro que deseas añadir a la lista\n")
    archivo=open("llibres.txt","r+")
    lista=(archivo.readlines())
    separador='|'
    import random
    for linea in lista:
        enlista=libro.lower() == linea.lower()
        if enlista==False:
            autor=input("Introduce el nombre le autor\n")
            publicacion=input("Introduce el año de publicacion\n")
            genero=input("Introduce el genero al que pertenece\n")
            libro=libro.title()
            autor=autor.title()
            genero=genero.title()
            codigo1 = random.randint(0, 90)
            codigo2=random.randint(10,60000)
            codigo3=random.randint(300,60000)
            codigo4=random.randint(0,10)
            codigo="|"+str("978")+"-"+str(codigo1)+"-"+str(codigo2)+"-"+str(codigo3)+"-"+str(codigo4)
            conjunto=libro+separador+autor+separador+publicacion+separador+genero+codigo
            lista.append(conjunto)
            lista.append('\n')
            print(" el libro se ha añadido a la lista correctamente")
            break       
    else:
        print("Ese libro ya se encuentra en nuestra lista")
            
    archivo=open("llibres.txt","w")
    archivo.writelines(lista)

añadir_libro()