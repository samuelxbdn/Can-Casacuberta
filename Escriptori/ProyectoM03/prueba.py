libros = ['Cien años de soledad', 'El principito', '1984']

# Función para añadir un libro a la lista
def anadir_libro(nuevo_libro):
    libros.append(nuevo_libro)
    for linea in libros:
        print(linea)

# Añadiendo libros a la lista
anadir_libro('La sombra del viento')
anadir_libro('Harry Potter y la piedra filosofal')

print(libros)