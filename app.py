from flask import Flask, render_template, request, redirect, url_for
import modelo

app = Flask(__name__)

@app.route('/')
def mostrar_pedidos():
    
    pedidos = modelo.listar_pedidos()
    return render_template('pedidos.html', pedidos=pedidos)

@app.route('/nuevo_pedido', methods=['GET', 'POST'])
def nuevo_pedido():
    if request.method == 'POST':
        nombre_cliente = request.form['nombre_cliente']
        producto = request.form['producto']
        cantidad = request.form['cantidad']
        
        modelo.crear_pedido(nombre_cliente, producto, cantidad)
        return redirect(url_for('mostrar_pedidos'))  
 
    return render_template('nuevo_pedido.html')

if __name__ == '__main__':
    app.run(debug=True)
