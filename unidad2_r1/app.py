import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crud.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET donde busca un nombre
@app.route('/', methods=['GET'])
def query_records():
    ProductosID = request.args.get('ProductosID')
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Productos')
    data = cursor.fetchall()
    for reg in data:
       registros.append(dict(reg))
    conn.close()
    return jsonify(json.dumps(registros))


@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO Productos(ProductosID, Nombre, Precio, Stock, Descripcion, FechaCreacion, FechaActualizacion, Categoria, IndiceProducto) VALUES(?,?,?,?,?,?,?,?,?)'
    cursor.execute(insert, [record['ProductosID'], record['Nombre'], record['Precio'], record['Stock'], record['Descripcion'], record['FechaCreacion'], record['FechaActualizacion'], record['Categoria'], record['IndiceProducto']])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
   
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM Productos WHERE ProductosID= ?'
    cursor.execute(delete, [record['ProductosID']])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'UPDATE Productos SET Nombre = ? WHERE ProductosID= ?'
    cursor.execute(delete, [record['Nombre'], record['ProductosID']])
    conn.commit()
    return jsonify(record)
app.run(debug=True)
