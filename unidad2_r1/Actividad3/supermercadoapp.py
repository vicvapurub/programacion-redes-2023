'''
    Nombre: Victor Manuel Ramirez Reyes
    Fecha: 23/22/2023
    Actividad III: I Programación Orientada a Objetos con Python

'''

from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def conectar_db():
    return sqlite3.connect('crud.db')

# Ruta para obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Productos')
    columnas = [columna[0] for columna in cursor.description]
    productos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    conn.close()
    return jsonify({'productos': productos})

# Ruta para obtener un producto por ID
@app.route('/productos/<int:producto_id>', methods=['GET'])
def obtener_producto(producto_id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Productos WHERE ProductoID = ?', (producto_id,))
    columnas = [columna[0] for columna in cursor.description]
    producto = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    conn.close()
    return jsonify({'producto': producto})

# Ruta para agregar un nuevo producto
@app.route('/productos', methods=['POST'])
def agregar_producto():
    nuevo_producto = request.json
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Productos (Nombre, Precio, Stock, Descripcion, Categoria, IndiceProducto,ProductoID) VALUES (?, ?, ?, ?, ?, ?,?)',
                   (nuevo_producto['Nombre'], nuevo_producto['Precio'], nuevo_producto['Stock'], nuevo_producto['Descripcion'],
                    nuevo_producto['Categoria'], nuevo_producto['IndiceProducto'], nuevo_producto['ProductoID']))
    conn.commit()
    nuevo_producto_id = cursor.lastrowid
    conn.close()
    return jsonify({'producto_id': nuevo_producto_id, 'mensaje': 'Producto agregado con éxito'})

# Ruta para actualizar un producto
@app.route('/productos/<int:producto_id>', methods=['PUT'])
def actualizar_producto(producto_id):
    producto_actualizado = request.json
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Productos SET Nombre = ?, Precio = ?, Stock = ?, Descripcion = ?, Categoria = ?, IndiceProducto = ? WHERE ProductoID = ?',
                   (producto_actualizado['Nombre'], producto_actualizado['Precio'], producto_actualizado['Stock'],
                    producto_actualizado['Descripcion'], producto_actualizado['Categoria'], producto_actualizado['IndiceProducto'], producto_id))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Producto actualizado con éxito'})

# Ruta para eliminar un producto
@app.route('/productos/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Productos WHERE ProductoID = ?', (producto_id,))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Producto eliminado con éxito'})

# Ruta para obtener todas las ventas
@app.route('/ventas', methods=['GET'])
def obtener_ventas():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Ventas')
    columnas = [columna[0] for columna in cursor.description]
    ventas = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    conn.close()
    return jsonify({'ventas': ventas})

# Ruta para obtener una venta por ID
@app.route('/ventas/<int:venta_id>', methods=['GET'])
def obtener_venta(venta_id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Ventas WHERE VentaID = ?', (venta_id,))
    columnas = [columna[0] for columna in cursor.description]
    venta = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    conn.close()
    return jsonify({'venta': venta})

# Ruta para agregar una nueva venta
@app.route('/ventas', methods=['POST'])
def agregar_venta():
    nueva_venta = request.json
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Ventas (ProductoID, ClienteID, Cantidad, Total, FechaVenta,) VALUES (?, ?, ?, ?, ?)',
                   (nueva_venta['ProductoID'], nueva_venta['ClienteID'], nueva_venta['Cantidad'], nueva_venta['Total'], nueva_venta['FechaVenta']))
    conn.commit()
    nueva_venta_id = cursor.lastrowid
    conn.close()
    return jsonify({'venta_id': nueva_venta_id, 'mensaje': 'Venta agregada con éxito'})

# Ruta para actualizar una venta
@app.route('/ventas/<int:venta_id>', methods=['PUT'])
def actualizar_venta(venta_id):
    venta_actualizada = request.json
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Ventas SET ProductoID = ?, ClienteID = ?, Cantidad = ?, Total = ?, FechaVenta = ? WHERE VentaID = ?',
                   (venta_actualizada['ProductoID'], venta_actualizada['ClienteID'], venta_actualizada['Cantidad'],
                    venta_actualizada['Total'], venta_actualizada['FechaVenta'], venta_id))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Venta actualizada con éxito'})

# Ruta para eliminar una venta
@app.route('/ventas/<int:venta_id>', methods=['DELETE'])
def eliminar_venta(venta_id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Ventas WHERE VentaID = ?', (venta_id,))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Venta eliminada con éxito'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
