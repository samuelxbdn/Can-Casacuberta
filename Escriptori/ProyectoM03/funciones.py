def login():
    import hashlib
    import sys
    flag=False
    intentos=0
    passwd=[]
    user=input("Buenos días, introduzca su nombre de usuario.\n")
    archivo=open("usuaris.txt","r")
    lista=(archivo.readlines())
    for linea in lista:
        registro=linea.split('|')
        if registro[0]==user:
            while flag==False:
                password=input("Introduce tu contraseña.\n")
                contraseña=hashlib.md5(password.encode())
                contraseña=contraseña.hexdigest()
                if contraseña in registro[1]:
                    print("Contraseña correcta.")
                    flag=True
                else:
                    intentos +=1
                    print("Contraseña incorrecta. Intentos restantes=", 3-intentos)
                    
                if intentos==3:
                    print("Has superado los 3 intentos.\n")
                    sys.exit()
    if flag==False:
        print("Nombre de usuario incorrecto.\n")
        login()
    return(user)

def listar_todos():
    archivo=open("llibres.txt","r")
    lista=(archivo.readlines())
    for linea in lista:
      datos=linea.split('|')
      print("-",datos[0])

def mostrar_libro():
    flag=False
    nombre=input("Escribe el titulo al que quieres acceder.\n")
    archivo=open("llibres.txt","r")
    lista=(archivo.readlines())
    for libro in lista:
        datos=libro.split('|')
        if nombre.lower() == datos[0].lower():
            print(libro)
            flag=True
    if flag==False:
        print("Ese libro no consta en nuestra lista.\n")


def añadir_libro():
    libro=input("Escribe el titulo del libro que deseas añadir a la lista.\n")
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
            print(" el libro se ha añadido a la lista correctamente.\n")
            break       
    else:
        print("Ese libro ya se encuentra en nuestra lista.\n")
            
    archivo=open("llibres.txt","w")
    archivo.writelines(lista)

def borrar ():
    libro=input("Escribe el titulo que deseas eliminar de la lista.\n")
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
                print("libro borrado de la lista correctamente.\n")
                break
    if flag==False:
        print("Ese libro no se encuentra en nuestra lista.\n")
    archivo=open("llibres.txt","w")
    archivo.writelines(lista)     
    
def editar_libro():
    libro=input("Escribe el titulo del libro que deseas editar de la lista.\n")
    archivo=open("llibres.txt","r+")
    lista=(archivo.readlines())
    for linea in lista:
        datos=linea.split('|')
        enlista=libro.lower() == datos[0].lower()
        if enlista==True:
            concepto=input("Indica el concepto a editar: Nombre del libro(1),Nombre del autor(2) o Año de publicación(3).\n")
            if int(concepto)==1:
                nombre=input("Introduce el nombre correcto del libro.\n")
                nombre=nombre.title()
                datos=linea.split('|')
                datos[0]=nombre
                modificado='|'.join(datos)
                lista.remove(linea)
                lista.append(modificado)
                archivo=open("llibres.txt","w")
                archivo.writelines(lista)
                print("Nombre de libro modificado correctamente.\n")

            if int(concepto)==2:
                nombre=input("Introduce el nombre correcto del autor.\n")
                nombre=nombre.title()
                datos=linea.split('|')
                datos[1]=nombre
                modificado='|'.join(datos)
                lista.remove(linea)
                lista.append(modificado)
                archivo=open("llibres.txt","w")
                archivo.writelines(lista)
                print("Nombre del autor modificado correctamente.\n")

            if int(concepto)==3:
                publicacion=input("Introduce el año correcto de publicación.\n")
                datos=linea.split('|')
                datos[2]=publicacion
                modificado='|'.join(datos)
                lista.remove(linea)
                lista.append(modificado)
                archivo=open("llibres.txt","w")
                archivo.writelines(lista)
                print("Año de publicación del libro modificado correctamente.\n")
    else:
        print("Ese libro no está en la lista.\n")
