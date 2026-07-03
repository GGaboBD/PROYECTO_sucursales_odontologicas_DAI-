from flask import Flask, jsonify, request

# Importar blueprints de entidades - - - - - - - - - - - - - - - - - - - from Entidades.citas import citas_bpfrom Entidades.expediente import expedientes_bp
from Entidades.paciente import paciente_bp
from Entidades.personal_administrativo import personal_admin_bp
from Entidades.rol import rol_bp
from Entidades.sucursal import sucursal_bp
from Entidades.ventas import ventas_bp 
from Entidades.citas import citas_bp
from Entidades.expediente import expedientes_bp

app = Flask(__name__)

# Registrar blueprints en servidor main -> app.py
app.register_blueprint(citas_bp)
app.register_blueprint(expedientes_bp)
app.register_blueprint(paciente_bp)
app.register_blueprint(personal_admin_bp)
app.register_blueprint(rol_bp)
app.register_blueprint(sucursal_bp)
app.register_blueprint(ventas_bp)

@app.get("/")
def inicio():
    return jsonify({
        "mensaje": "Bienvenido a la app de biblioteca",
        "version": "1.0",
        "endpoints": [
            "-------------------------",
            "GET    /ventas",
            "GET    /ventas/<id>",
            "POST   /ventas",
            "-------------------------",
            "GET    /sucursal",
            "GET    /sucursal/<id>",
            "POST   /sucursal",
            "-------------------------",
            "GET    /expediente",
            "GET    /expediente/<id>",
            "POST   /expediente",
            "-------------------------",
            "GET    /personal_admin",
            "GET    /personal_admin/<id>",
            "POST   /personal_admin",
            "-------------------------",
            "GET    /rol",
            "GET    /rol/<id>",
            "POST   /rol",
            "-------------------------",
            "GET    /paciente",
            "GET    /paciente/<id>",
            "POST   /paciente",
            "-------------------------",
            "GET    /citas",
            "GET    /citas/<id>",
            "POST   /citas",
            "-------------------------",
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)