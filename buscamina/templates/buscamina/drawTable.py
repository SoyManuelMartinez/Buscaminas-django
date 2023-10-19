from flask import Flask, request, render_template

app = Flask(__name)

@app.route('/', methods=['GET', 'POST'])
def generador_tabla():
    tabla = None

    if request.method == 'POST':
        filas = int(request.form['filas'])
        columnas = int(request.form['columnas'])
        tabla = generar_tabla(filas, columnas)

    return render_template('formulario_tabla.html', tabla=tabla)

def generar_tabla(filas, columnas):
    tabla = [['Fila {} Col {}'.format(i, j) for j in range(1, columnas + 1)] for i in range(1, filas + 1)]
    return tabla

if __name__ == '__main__':
    app.run()