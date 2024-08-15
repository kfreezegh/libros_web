import csv
from Libro import Libro

class BaseLibros:
    diccionario = {}
    categorias  = {}
    did = {}

    def agregarLibroTitulo(self,libro:Libro):
        titulo = libro.titulo.lower()
        self.actualizaDiccionario(titulo,libro)
        #agregar autor
        autor = libro.autor
        self.actualizaDiccionario(autor,libro)

    def actualizaDiccionario(self,llave:str,libro:Libro):
        if llave in self.diccionario:
            self.diccionario[llave].append(libro)
        else:
            self.diccionario[llave] = [libro]
        palabras = llave.split(" ")
        for palabra in palabras:
            if palabra in self.diccionario:
                self.diccionario[palabra].append(libro)
            else:
                self.diccionario[palabra] = [libro]

    def __init__(self,archivo:str):
        lista_registros = self.carga_libros_csv(archivo)
        self.did = {}
        for registro in lista_registros:
            id = registro[0]
            imagen = registro[1]
            url_imagen = registro[2]
            titulo = registro[3]
            autor = registro[4]
            id_categoria = registro[5]
            categoria = registro[6]
            self.crea_catalogo_categorias(id_categoria,categoria)
            libro = Libro(id,imagen,url_imagen,titulo,autor,id_categoria)
            self.agregarLibroTitulo(libro)
            self.agregalibroId(libro)


    def desplegar(self):
        for llave, valor in self.diccionario.items():
            print(f"{llave}\n__________________")
            for libro in valor:
                print(libro) 


    def carga_libros_csv(self,archivo:str)->list:
        #aqui va el codigo
        lista_registros = []
        with open(archivo,"r",encoding="utf-8") as a:
            reader = csv.reader(a)
            for renglon in reader:         
                lista_registros.append(renglon)
        return lista_registros
    

    def obtenerLibro(self,llave:str)->list:
        llave = llave.lower()
        lista = []
        if llave in self.diccionario:
            lista = self.diccionario[llave]
        return lista
    

    def get_libros(self):
        d = {}
        for titulo in self.diccionario:
            for libro in self.diccionario[titulo]:
                if libro.id not in d:
                    d[libro.id] = libro
 
        lista = [v for v in d.values()]
        return lista

        

    def crea_catalogo_categorias(self,id_cat:str,cat:str):
        id_cat = int(id_cat)
        if id_cat not in self.categorias:
            self.categorias[id_cat] = cat
    
    def agregalibroId(self,libro):
        if libro.id not in self.did:
            self.did[libro.id] = libro
    
    def get_libro(self,id):
        if id in self.did:
            return self.did[id]
        else:
            return None
               

if __name__ == "__main__":
    #lista = carga_libros_csv("booklist2000.csv")
    base  = BaseLibros("libros_web/booklist2000.csv")
    #base.desplegar()
    lista_libros = base.obtenerLibro("Gallery")
    for libro in lista_libros:
        print(libro)
    
