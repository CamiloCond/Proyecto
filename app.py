from flask import Blueprint, render_template, request, redirect, url_for
import models.pedidos as modelo

pedidos_bp = Blueprint('pedidos', __name__)

@pedidos_bp.route('/')
def mostrar_pedidos():
    pedidos = modelo.listar_pedidos()
    return render_template('pedidos.html', pedidos=pedidos)

@pedidos_bp.route('/nuevo_pedido', methods=['GET', 'POST'])
def nuevo_pedido():
    if request.method == 'POST':
        nombre_cliente = request.form.get('nombre_cliente', '').strip()
        producto = request.form.get('producto', '').strip()
        cantidad = request.form.get('cantidad', '').strip()

        if not nombre_cliente or not producto or not cantidad.isdigit():
            return render_template('nuevo_pedido.html', error="Todos los campos son obligatorios.")

        modelo.crear_pedido(nombre_cliente, producto, int(cantidad))
        return redirect(url_for('pedidos.mostrar_pedidos'))

    return render_template('nuevo_pedido.html')

