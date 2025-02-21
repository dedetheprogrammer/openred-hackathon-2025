import requests
from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)

HOST = "127.0.0.1" # Cambiar a la URL de donde se despliegue
PORT = 8080 # # Cambiar al puerto de donde se despliegue

@app.route("/api/test")
def data_process():
    # Procesar datos
    return jsonify( {"name" : "John", "surname": "Doe"} )

@app.route("/api/process", methods=['POST'])
def data_process():
    # Procesar datos
    try:
        data = request.text()
        return { data }, 200
    except Exception as e:
        print("Error al procesar los datos:", e)
        return {"error": "Server internal error"}, 500



# == Starting the server =================================================
# Esta sección se ejecuta cuando el archivo es ejecutado como script (python app.py)
if __name__ == '__main__':

    # Arranca el servidor en el host y puerto especificados
    print(f"Serving server at http://{HOST}:{PORT}, you can use the API at this address.")
    # Llama a la función `serve` para iniciar el servidor web
    serve(app, host=HOST, port=PORT)