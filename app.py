from flask import Flask, render_template, request

app = Flask(__name__)

servicios = [
    {"nombre": "Stand de Glitter y Maquillaje Artisstico",
     "descripcion": "Nuestro Stand de Glitter ofrece una experiencia completa de brillo y color con glitter en polvo o gel, gemas, strass, piedras y polvo de hadas en variados colores, texturas y tamaños. Incluye pelos locos con pintura de brillo, maquillaje artístico para niños y adultos, y tatuajes personalizados. Todos nuestros productos son hipoalergénicos y el servicio viene equipado con banner, cartel y espejo hollywood." },
    {"nombre": "Animacion Infantil 1, 2 y 3 horas", 
     "descripcion": "incluye juegos de destreza, habilidad y competencia acorde a la edad del grupo, maquillaje artístico para todos los nenes, también glitter y maquina de burbujas. En esta opcion, si querés te ayudo  a organizar el momento de la torta y piñata, tambien servirle a los nenes la comida y gaseosa que tengas, eso depende de cada familia, llevo disfraz de panchero." },
    {"nombre": "Fotografía Profesional",
     "descripcion": "Servicio de fotografía Profesional. Fotos ilimitadas, todas editadas en alta calidad y entregadas en formato digital por Google Drive."},

    ]

fotos = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg","8.jpg","9.jpg"]

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/")
def inicio():
    return render_template("inicio.html", fotos=fotos )

@app.route("/servicios")
def mostrar_servicios():
    return render_template("servicios.html", servicios=servicios)
if __name__ == "__main__":
    app.run(debug=True)

