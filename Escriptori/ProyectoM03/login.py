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

login()