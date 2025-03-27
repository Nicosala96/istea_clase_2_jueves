from Clases import Libro
import pandas as pd

libros = pd.read_csv("Libros")

generos_literarios = [
            "Ficcion","Ciencia Ficcion","Fantasia","Romance","Clasico","Juvenil","Historica","Misterio","Terror","Drama",
            "Distopia","Parodia","Aventura","Policiaco","Biografia","Ensayo","Poesia","Mitologia","Gotico","RealismoMagico"
        ]


lista_libros = [Libro(row['titulo'], row['autor'], row['genero'], row['puntuacion']) for _, row in libros.iterrows()]

while True:
    consulta = input("¿Deseas agregar un libro, buscar un libro o una recomendacion? Usa"
                     " las siguientes opciones (agregar/buscar/recomendacion/salir)\n").lower()

    if consulta not in ["agregar", "buscar", "recomendacion","salir"]:
        print("Error. Use una de las opciones indicadas anteriormente")

    elif consulta == "salir":
        break

    elif consulta == "agregar":
        datos_nuevos = input("Ingresa el titulo, autor, genero y puntuacion separados por comas\n")
        titulo, autor, genero, puntuacion = [dato.strip() for dato in datos_nuevos.split(",")]


        nuevo_libro = pd.DataFrame({
                "titulo": [titulo],
                "autor": [autor],
                "genero": [genero],
                "puntuacion": [float(puntuacion)]
            })
        libros = pd.concat([libros, nuevo_libro], ignore_index=True)
        libros.to_csv("Libros", index=False)
        print("Libro agregado exitosamente.")

    elif consulta == "buscar":
        while True:
            consulta_genero = input("¿Que genero estabas buscando?\n").strip().capitalize()
            if consulta_genero not in generos_literarios:
                print("Elige otra opcion")
            else:
                libros_encontrados = [libro for libro in lista_libros if libro.genero.strip() == consulta_genero]

                if libros_encontrados:
                    print(f"Libros del género '{consulta_genero}':")
                    for libro in libros_encontrados:
                        print(f"- {libro.titulo} de {libro.autor}")
                else:
                    print(f"No se encontraron libros del género '{consulta_genero}'.")
                break
    else:
        consulta_genero = input("¿Que genero estabas buscando?\n").strip().capitalize()
        if consulta_genero not in generos_literarios:
            print("Elige otra opcion")
        else:
            libros_encontrados = [libro for libro in lista_libros if libro.genero.strip() == consulta_genero]
            libros_encontrados.sort(key=lambda libro: libro.puntuacion, reverse=True)
            for libro in libros_encontrados:
                print(f"- {libro.titulo} de {libro.autor} con puntuacion de {libro.puntuacion}")








