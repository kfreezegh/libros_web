from flask import Flask, render_template, request, redirect, url_for
from BaseLibros import BaseLibros

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/por_titulo')
def por_titulo():
    listado = bd.get_libros()
    listado = sorted(listado, key=lambda x:x.titulo)
    categorias = bd.categorias
    return render_template('tabla.html',lista=listado,dcat=categorias,orden="Titulo")

@app.route('/por_autor')
def por_autor():
    listado = bd.get_libros()
    listado = sorted(listado, key=lambda x:x.autor)
    categorias = bd.categorias
    return render_template('tabla.html',lista=listado,dcat=categorias,orden="Autor")

@app.route('/por_categoria')
def por_categoria():
    listado = bd.get_libros()
    listado = sorted(listado, key=lambda x:x.id_categoria)
    categorias = bd.categorias
    return render_template('tabla.html',lista=listado,dcat=categorias,orden="Categoria")

@app.route("/buscar_libro",methods=["POST"]) # home o raiz del sitio web
def buscar_libro():
    #tomar texto de la forma
    lista_libros = []
    if request.method == "POST":
        #texto = request.form.get("texto")
        texto = request.form["texto"]
        #texto = request.form
        texto = texto.lower()
        print(texto)
        #buscarlo en la bd
        lista_libros = bd.obtenerLibro(texto)
        categorias = bd.categorias
    #si se encuentra, publicarlo
    return render_template("resultado_libros.html",lista=lista_libros,dcat=categorias)

@app.route("/about") # pagina con informacion sobre este sitio
def about():
    return '<html><head><title>Sobre esta pagina</title></head><body>Todo sobre este sitio web. volver a la pagina de <a href="/">hola mundo</a></body></html>'

@app.route("/libro/<id>")
def por_id(id):
    if id in bd.did: #buscanmos en diccionario en ids
        book = bd.get_libro(id)
        print(book.titulo)
        return render_template('libro.html',libro=book)
    return render_template('no_encontrado.html')


if __name__ == '__main__':
    bd = BaseLibros("booklist2000.csv")
    app.run(debug=True)
