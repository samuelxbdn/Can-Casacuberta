def listar_todos():
    archivo=open("llibres.txt","r")
    lista=(archivo.readlines())
    for linea in lista:
      datos=linea.split('|')
      print("-",datos[0])
listar_todos()