from flask import Flask, jsonify, request
from Entidades.ventas import ventas_bp 
from Entidades.rol import rol_bp 

app = Flask(__name__)

app.register_blueprint(ventas_bp)

@app.get("/")
def inicio():
    return jsonify({
        "mensaje": "Bienvenido a la app de biblioteca",
        "version": "1.0",
        "endpoints": [
            "GET    /ventas",
            "GET    /ventas/<id>",
            "POST   /ventas",
            "GET    /sucursal",
            "GET    /sucursal/<id>",
            "POST   /sucursal"
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)