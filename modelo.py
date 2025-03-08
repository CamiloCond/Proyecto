# Archivo: modelo.py
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


from flask import Flask, render_template
from modelo import db, Usuario, Pedido

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pedidos.db'
db.init_app(app)

@app.route('/')
def index():
    return "Sistema de Gestión de Pedidos de Calzado"

if __name__ == '__main__':
    app.run(debug=True)


from modelo import db, Pedido

def crear_pedido(cliente_id, estado):
    nuevo_pedido = Pedido(cliente_id=cliente_id, estado=estado)
    db.session.add(nuevo_pedido)
    db.session.commit()
    return nuevo_pedido


def crear_pedido(nombre_cliente, producto, cantidad):
    
    pedido = {
        'nombre_cliente': nombre_cliente,
        'producto': producto,
        'cantidad': cantidad,
        'estado': 'Pendiente'
    }
    return pedido



# Lista para almacenar pedidos 
pedidos = []

def listar_pedidos():
    return pedidos

def crear_pedido(nombre_cliente, producto, cantidad):
    nuevo_pedido = {
        'nombre_cliente': nombre_cliente,
        'producto': producto,
        'cantidad': cantidad,
        'estado': 'Pendiente'  
    }
    pedidos.append(nuevo_pedido)
import json


FILE_PATH = 'pedidos.json'


def cargar_pedidos():
    try:
        with open(FILE_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  

# Guardar los pedidos en el archivo
def guardar_pedidos(pedidos):
    with open(FILE_PATH, 'w') as f:
        json.dump(pedidos, f)

# Función para listar los pedidos
def listar_pedidos():
    return cargar_pedidos()

# Función para crear un nuevo pedido
def crear_pedido(nombre_cliente, producto, cantidad):
    pedidos = cargar_pedidos()
    nuevo_pedido = {
        'nombre_cliente': nombre_cliente,
        'producto': producto,
        'cantidad': cantidad,
        'estado': 'Pendiente'
    }
    pedidos.append(nuevo_pedido)
    guardar_pedidos(pedidos)

