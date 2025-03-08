# archivo: modelo.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    estado = db.Column(db.String(50), nullable=False)

# archivo: app.py
from flask import Flask, render_template, jsonify, request
from modelo import db, Usuario, Pedido

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pedidos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Evitar advertencias de SQLAlchemy
db.init_app(app)

@app.route('/')
def index():
    return "Sistema de Gestión de Pedidos de Calzado"

# Rutas para API
@app.route('/api/pedidos', methods=['GET'])
def listar_pedidos():
    pedidos = Pedido.query.all()  # Consulta eficiente a la base de datos
    return jsonify([pedido.to_dict() for pedido in pedidos])

@app.route('/api/pedidos', methods=['POST'])
def crear_pedido():
    data = request.get_json()
    cliente_id = data.get('cliente_id')
    estado = data.get('estado', 'Pendiente')  # Estado por defecto: Pendiente
    nuevo_pedido = Pedido(cliente_id=cliente_id, estado=estado)
    db.session.add(nuevo_pedido)
    db.session.commit()
    return jsonify(nuevo_pedido.to_dict()), 201

# Agregar método para convertir a diccionario
def to_dict(self):
    return {
        'id': self.id,
        'cliente_id': self.cliente_id,
        'estado': self.estado
    }

# Enlazar el método to_dict a la clase Pedido
Pedido.to_dict = to_dict

if __name__ == '__main__':
    app.run(debug=True)



